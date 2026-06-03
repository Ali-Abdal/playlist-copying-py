import ytmusicapi


class Youtube:
    def __init__(self):
        self.yt = ytmusicapi.YTMusic("browser.json")

    def get_playlists(self):
        playlists_all_data = self.yt.get_library_playlists()
        playlists_wanted_data = []

        for p in playlists_all_data:
            playlist_data = {}
            playlist_data["title"] = p["title"]
            playlist_data["playlistId"] = p["playlistId"]
            playlists_wanted_data.append(playlist_data)

        return playlists_wanted_data

    def get_songs(self, playlistID):
        songs_all_data = (self.yt.get_playlist(playlistId=playlistID, limit=None))[
            "tracks"
        ]
        songs_wanted_data = []

        for s in songs_all_data:
            if not s["isAvailable"]:
                continue
            song_data = {}
            song_data["title"] = s["title"]
            song_data["artist"] = s["artists"][0]["name"]
            songs_wanted_data.append(song_data)

        return songs_wanted_data
