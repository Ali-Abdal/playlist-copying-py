import ytmusicapi
import os
from youtube import Youtube
from spotify import Spotify
from dotenv import load_dotenv


def main():
    print("===Starting Programm===\n\n")  # debug messages

    # makes sure browser.json exists
    try:
        with open("browser.json", "r") as fh:
            pass
    except FileNotFoundError:
        init_browserjson()

    yt = Youtube()

    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not all([client_id, client_secret]):
        print("Error: Missing Spotify credentials in .env file.")
        return

    playlists = yt.get_playlists()

    print("====== Playlists ======\n")

    playlist_titles = [p["title"] for p in playlists]

    for t in playlist_titles:
        print(t)

    print("=======================\n")

    while True:
        print(
            "====== Options ======\nEnter exact playlist name to copy\nq to quit\n======================="
        )
        user_input = input(">>> ")

        if user_input == "q":
            exit()

        if user_input in playlist_titles:
            sp = Spotify(client_id, client_secret)

            for p in playlists:
                if user_input == p["title"]:
                    playlistID = p["playlistId"]

            songs = yt.get_songs(playlistID=playlistID)

            uris = sp.get_tracks_uris(songs)

            with open("playlist.txt", "w") as fh:
                for uri in uris:
                    fh.write(uri + "\n")

            print("Done! Open playlist.txt and paste into Spotify.")
            exit()


# Creats the browser.json file from input in headers_input.text
def init_browserjson():
    print("===Intilizing browser.json===")  # debug messages

    # creats headers_input.txt if not found
    try:
        with open("headers_input.txt", "r") as fh:
            user_input = fh.read()
    except FileNotFoundError:
        with open("headers_input.txt", "w") as fh:
            fh.write("")
        print(
            "Error: Please make sure to paste your browser headers into file: headers_input.txt"
        )

    # validates headers_input content
    try:
        ytmusicapi.setup(filepath="browser.json", headers_raw=user_input)
    except ytmusicapi.exceptions.YTMusicUserError:
        print(
            "Error: Make sure headers_input file is not empty and includes the following entries:  x-goog-authuser, cookie. Please try a different request (such as /browse) and make sure you are logged in"
        )


if __name__ == "__main__":
    main()
