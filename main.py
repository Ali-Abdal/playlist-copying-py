import ytmusicapi
import os
from youtube import Youtube
from spotify import Spotify
from dotenv import load_dotenv


def main():
    print("===Starting Programm===")  # debug messages

    # makes sure browser.json exists
    try:
        with open("browser.json", "r") as fh:
            pass
    except FileNotFoundError:
        init_browserjson()
        return

    yt = Youtube()

    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not all([client_id, client_secret]):
        print("Error: Missing Spotify credentials in .env file.")
        return

    # testing
    sp = Spotify(client_id, client_secret)

    playlistID = "PLDCMizaqqwzEN0-wl2Vz8zrrX-uArANP5"
    songs = yt.get_songs(playlistID=playlistID)

    sp.get_track_uris(songs)
    #


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
