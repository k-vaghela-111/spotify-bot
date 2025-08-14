# 🎧 Spotify Top 100 Playlist Bot

Create a nostalgic playlist in seconds! Just enter a year, and this bot will fetch the top 100 songs from that era and build a Spotify playlist for you.

---

## 🚀 Features

- 🔍 Scrapes Billboard Top 100 songs for any year
- 🎵 Automatically creates a Spotify playlist
- 🧠 Smart search for matching tracks
- 💾 Saves playlist to your Spotify account

---

## 🛠️ Tech Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Core scripting                   |
| BeautifulSoup | Web scraping Billboard data      |
| Spotipy       | Spotify API integration          |
| dotenv        | Secure credential management     |

---


## 🧠 How It Works

1. Scrapes Billboard's Top 100 songs for the given year using BeautifulSoup.
2. Searches each song on Spotify using the Spotipy library.
3. Creates a new playlist in your Spotify account.
4. Adds all found tracks to the playlist.
5. Saves the playlist with a name like `Top 100 of 2005`.

---



cd spotify-bot
pip install -r requirements.txt
