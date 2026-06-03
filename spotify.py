import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


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

    # not finished you need also to clean track names
    def get_track_uris(self, songs):
        uris = []

        for s in songs:
            title = s["title"]
            artist = s["artist"]
            query = f"{title} {artist}"

            result = self.sp.search(q=query, type="track", limit=1)
            print(result)
            break

        # return uris
