#!/usr/bin/env python3
"""
Minimal Spotify Web API client (stdlib + requests only).

Two modes:
  Client(user=False)  -> client-credentials token; enough for /albums, /tracks (enrich_labels.py)
  Client(user=True)   -> authorization-code token with refresh; needed for playback control and
                         currently-playing (collect_autoplay.py) and for reading playlists
                         (dump_playlist.py).

Environment:
  SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET   from https://developer.spotify.com/dashboard
  SPOTIFY_REDIRECT_URI                        default http://127.0.0.1:8888/callback (add the SAME
                                              value to the app's Redirect URIs in the dashboard)
  SPOTIFY_TOKEN_FILE                          where the user token is cached (default:
                                              tools/dm_autoplay/.spotify_token.json; gitignored)

First user-mode run prints an authorize URL: open it in the browser that is logged into the
experiment account, approve, then paste the full redirected URL back into the terminal.
"""
from __future__ import annotations
import base64
import json
import os
import sys
import time
import urllib.parse

import requests

API = "https://api.spotify.com/v1"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
DEFAULT_SCOPES = (
    "user-read-playback-state user-modify-playback-state user-read-currently-playing "
    "user-read-recently-played playlist-read-private playlist-read-collaborative"
)


def _creds():
    cid = os.environ.get("SPOTIFY_CLIENT_ID")
    sec = os.environ.get("SPOTIFY_CLIENT_SECRET")
    if not cid or not sec:
        sys.exit("Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET (developer.spotify.com/dashboard).")
    return cid, sec


def _basic_header():
    cid, sec = _creds()
    return {"Authorization": "Basic " + base64.b64encode(f"{cid}:{sec}".encode()).decode()}


class Client:
    def __init__(self, user: bool = True, scopes: str = DEFAULT_SCOPES, token_file: str | None = None):
        self.user = user
        self.scopes = scopes
        self.token_file = token_file or os.environ.get(
            "SPOTIFY_TOKEN_FILE", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".spotify_token.json"))
        self.redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI", "http://127.0.0.1:8888/callback")
        self._tok: dict = {}
        self._session = requests.Session()
        if user:
            self._load()
            if not self._tok.get("refresh_token"):
                self._authorize_interactive()
        else:
            self._client_credentials()

    # ---------------- token handling ----------------
    def _load(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, encoding="utf-8") as f:
                self._tok = json.load(f)

    def _save(self):
        with open(self.token_file, "w", encoding="utf-8") as f:
            json.dump(self._tok, f, indent=2)
        try:
            os.chmod(self.token_file, 0o600)
        except OSError:
            pass

    def _set(self, resp_json: dict):
        self._tok.update(resp_json)
        self._tok["expires_at"] = time.time() + int(resp_json.get("expires_in", 3600)) - 60
        if self.user:
            self._save()

    def _client_credentials(self):
        r = self._session.post(TOKEN_URL, headers=_basic_header(), data={"grant_type": "client_credentials"}, timeout=30)
        r.raise_for_status()
        self._set(r.json())

    def _authorize_interactive(self):
        cid, _ = _creds()
        q = urllib.parse.urlencode({
            "client_id": cid, "response_type": "code", "redirect_uri": self.redirect_uri,
            "scope": self.scopes, "show_dialog": "true"})
        print("\nOpen this URL in the browser logged into the EXPERIMENT account, approve, then paste the\n"
              "full URL you were redirected to (it will start with the redirect URI):\n")
        print(AUTH_URL + "?" + q + "\n")
        redirected = input("Redirected URL: ").strip()
        code = urllib.parse.parse_qs(urllib.parse.urlparse(redirected).query).get("code", [None])[0]
        if not code:
            sys.exit("No ?code= in the pasted URL.")
        r = self._session.post(TOKEN_URL, headers=_basic_header(), data={
            "grant_type": "authorization_code", "code": code, "redirect_uri": self.redirect_uri}, timeout=30)
        r.raise_for_status()
        self._set(r.json())

    def _refresh(self):
        if not self.user:
            self._client_credentials()
            return
        r = self._session.post(TOKEN_URL, headers=_basic_header(), data={
            "grant_type": "refresh_token", "refresh_token": self._tok["refresh_token"]}, timeout=30)
        r.raise_for_status()
        j = r.json()
        j.setdefault("refresh_token", self._tok["refresh_token"])
        self._set(j)

    def _headers(self):
        if time.time() >= self._tok.get("expires_at", 0):
            self._refresh()
        return {"Authorization": "Bearer " + self._tok["access_token"]}

    # ---------------- requests ----------------
    def request(self, method: str, path: str, params=None, json_body=None, retries: int = 6):
        url = path if path.startswith("http") else API + path
        for attempt in range(retries):
            r = self._session.request(method, url, headers=self._headers(), params=params, json=json_body, timeout=30)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", "5")) + 1
                print(f"[rate-limited] sleeping {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            if r.status_code == 401 and attempt == 0:
                self._refresh()
                continue
            if r.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            if r.status_code in (200, 201, 202, 204):
                return r
            raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text[:300]}")
        raise RuntimeError(f"{method} {path}: gave up after {retries} attempts")

    def get(self, path, params=None):
        r = self.request("GET", path, params=params)
        return None if r.status_code == 204 or not r.content else r.json()

    def put(self, path, json_body=None, params=None):
        return self.request("PUT", path, params=params, json_body=json_body)

    def post(self, path, json_body=None, params=None):
        return self.request("POST", path, params=params, json_body=json_body)
