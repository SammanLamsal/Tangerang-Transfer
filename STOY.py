from getpass import getuser
from tkinter.constants import CENTER
import spotipy 
from bottle import route, run, request
import tkinter as tk
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy.util as util
import requests
import creds

# username = usernameEntry.get() and playlistID = linkEntry.get()[34:56] in some command
# after getting user and link, cut the link to just get the id using ^
# learn how to hide client id and secret and stuff

global usernameEntry
global linkEntry 

def get_playlist_tracks(username, playlistID):
    songAndArtist = []
    auth_manager = SpotifyClientCredentials(creds.clientID, creds.clientSecret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results = sp.user_playlist_tracks(username,playlistID)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    for track in tracks:
        for artist in track['track']['album']['artists']:
            songAndArtist = track['track']['name'] + " by " + artist['name']
            print(songAndArtist)

def getUserAndLink():
    username = usernameEntry.get()
    playlistID = linkEntry.get()[34:56]
    get_playlist_tracks(username, playlistID)

def openStoyGui():
    root1 = tk.Toplevel()
    root1.title("SPOTIFY TO YOUTUBE")
    root1.geometry("800x800")
    root1.resizable(height = None, width = None)

    canvas1 = tk.Canvas(root1, bg = "#263")
    canvas1.pack(fill="both", expand="true")

    youtubeAuthenticateBtn = tk.Button(canvas1, text = "LOG IN WITH YOUTUBE", command = getUserAndLink)
    youtubeAuthenticateBtn.place(x = 325, y = 450)

    linkEntry = tk.Entry(root1, justify=CENTER)
    canvas1.create_window(200, 140, window=linkEntry)
    linkEntry.place(x = 500, y = 525, anchor=CENTER)

    linkTxt = canvas1.create_text(500, 700, anchor = CENTER, text = "INPUT SPOTIFY PLAYLIST LINK")
    
    canvas1.create_window(200, 140, window=usernameEntry)
    usernameEntry.place(x = 200, y = 525, anchor=CENTER)

    usernameTxt = canvas1.create_text(200, 700, anchor = CENTER, text = "INPUT SPOTIFY USERNAME")

    root1.mainloop()

