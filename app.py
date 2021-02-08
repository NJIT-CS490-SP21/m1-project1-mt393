from flask import Flask, render_template
import os
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv

load_dotenv('music.env')

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

app = Flask(__name__)

artists=['4UXqAaa6dQYAk18Lv7PEgX', "3hOdow4ZPmrby7Q1wfPLEy", "3MZsBdqDrRTJihTHQrO6Dq"]

@app.route('/')
def hello_world():
    artist = artists[random.randint(0,2)]
    songNum = random.randint(1,5)
    topTracks = sp.artist_top_tracks(artist)
    trackName = topTracks['tracks'][songNum]['name']
    trackAudio = topTracks['tracks'][songNum]['preview_url']
    trackArt = topTracks['tracks'][songNum]['album']['images'][0]['url']
    artistName = topTracks['tracks'][songNum]['album']['artists'][0]['name']
    print('Track name: ' + trackName)
    return render_template(
        "index.html",
        song = trackName,
        image = trackArt,
        audio = trackAudio,
        name = artistName
)

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
)
