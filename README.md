# YouTube Music → Spotify Playlist Copier

A personal tool that makes copying playlists from YouTube Music to Spotify much easier. Instead of manually searching for each song, the app fetches your YouTube Music playlists, searches for each track on Spotify, and outputs a list of Spotify URIs that you can paste directly into any Spotify playlist.

## How It Works

1. Authenticates with your YouTube Music account using browser headers
2. Displays your YouTube Music playlists in the terminal
3. You pick which playlist to copy
4. The app searches Spotify for each track
5. All found tracks are written to `playlist.txt` as Spotify URIs
6. You paste the URIs into a Spotify playlist manually

---

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. YouTube Music Authentication

YouTube Music has no official API, so this app authenticates by using your browser's request headers — essentially proving to YouTube Music that you're logged in.

**How to get your headers:**

1. Open Chrome and go to [music.youtube.com](https://music.youtube.com)
2. Make sure you're logged in
3. Press `F12` to open DevTools
4. Go to the **Network** tab
5. Refresh the page
6. In the filter box, type `browse` and click on any request that appears
7. On the right side, scroll to the **Request Headers** section
8. Copy everything from `accept: */*` to the end of the section
9. Paste the copied headers into `headers_input.txt`

On first run, the app will read `headers_input.txt` and generate a `browser.json` file that it uses for authentication from that point on.

> **Note:** Browser headers do expire. If your playlists are not showing up in the terminal and you know you have playlists, your headers have likely expired. To fix this: delete `browser.json`, paste fresh headers into `headers_input.txt`, and run the app again.

### 3. Spotify Setup

This app uses the Spotify Web API to search for tracks. You need to create a free Spotify developer app to get credentials.

**Steps:**

1. Go to [developer.spotify.com](https://developer.spotify.com) and log in with your Spotify account
2. Click **Create App**
3. Fill in any app name and description
4. Set the Redirect URI to `http://127.0.0.1:8888/callback`
5. Check **Web API** and agree to the terms
6. Once created, go to **Settings** to find your `Client ID` and `Client Secret`

**Add your credentials to `.env`:**

```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

You can use `.env.example` as a template just copy it to `.env` and fill in your values.

---

## Copying a Playlist to Spotify

1. Run the app:
```bash
python main.py
```
2. Your YouTube Music playlists will be displayed in the terminal
3. Enter the name of the playlist you want to copy when prompted
4. Wait for the app to search Spotify for each track
5. Open `playlist.txt` — it will contain all found Spotify URIs
6. Open the **Spotify desktop app** and create a new empty playlist
7. Select all URIs in `playlist.txt` (`Ctrl+A` then `Ctrl+C`)
8. Click on your new playlist and press `Ctrl+V` to paste
9. Spotify will automatically add all the tracks

> **Note:** The Spotify desktop app is required for pasting URIs. The web player does not support this.

---

## Accuracy

Sometimes the wrong song gets copied this usually happens with tracks that have messy titles or aren't available on Spotify. The app will skip tracks it can't find and print them in the terminal. Overall it's still significantly faster than copying playlists manually.

---

## Notes

This app was made primarily for personal use to quickly migrate my own playlists. As a result, the code lacks comments in most places and was written with the goal of getting it running as fast as possible rather than being a polished product. Use it as-is or feel free to improve it.
