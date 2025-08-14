import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date=input("which year you want to travel to ? input date in formate of YYYY-MM-DD ")
URL=f"https://www.billboard.com/charts/hot-100/{date}/"
year=date.split("-")[0]

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response=requests.get(URL,headers=header).text


soup=BeautifulSoup(response,"html.parser")

song_list=[song.getText().strip() for song in soup.select("li ul li h3")]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="a5f19f5d89d44164a8d9af812feb9b13",
        client_secret="c6a3f3a878bb4f57af71411645139a55",
        show_dialog=True,
        cache_path="token.txt",
        username="Karmrajsinh",
    )
)

user_id=sp.current_user()["id"]

uri = []
for song in song_list:
    song_response = sp.search(q=f"year:{year} track:{song}",type="track")
    try:
        uri.append(song_response["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Making Playlist

name = f"{date} Billboard top 100"

playlist = sp.user_playlist_create(user=user_id,
                                      name=name,
                                      public=False)
sp.playlist_add_items(playlist["id"],uri)

print("Your playlist successfully created")


