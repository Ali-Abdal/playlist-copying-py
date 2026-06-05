import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re


class Spotify:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret,
            )
        )

    def clean_title(self, title):
        title = re.sub(r"\(.*?\)", "", title)
        title = re.sub(r"\[.*?\]", "", title)
        return title.strip()

    def search_track(self, title, artist):
        title = self.clean_title(title)
        query = f"{title} {artist}"
        result = self.sp.search(q=query, type="track", limit=1)
        return result

    def get_tracks_uris(self, songs):
        uris = []

        for s in songs:
            title = s["title"]
            artist = s["artist"]
            result = self.search_track(title, artist)
            items = result["tracks"]["items"]
            if items:
                uri = items[0]["uri"]
                uris.append(uri)

        return uris
