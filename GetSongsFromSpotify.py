import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests


def search_youtube(query):
    # Set up the YouTube API endpoint
    endpoint = "https://www.googleapis.com/youtube/v3/search"

    # Set up the request parameters
    params = {
        "part": "id",
        "q": query,
        "type": "video",
        "key": "AIzaSyAY4IK9hmFPHofO8z6cHp9G4yGdsf9lfcY" # replace with your own YouTube API key

    }

    # Send the GET request
    response = requests.get(endpoint, params=params)
    # Parse the response to extract the video links
    results = response.json()["items"]
    video_links = []
    for result in results:
        video_id = result["id"]["videoId"]
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        video_links.append(video_link)

    return video_links


scope = "playlist-read-private"
client_id = "f004b795421145b9bf9f4f12c7d79b84"
client_secret = "a5d98e6a380a49788c0647d5ae5f3358"
redirect_uri = "http://localhost:8000/callback"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))


# rest of the code goes here


# set the playlist ID
playlist_id = "00t6gvig2IAlcXnTXqksVr"

# get the playlist information
playlist = sp.playlist(playlist_id)

# extract the track information and print the track names

tracks = playlist["tracks"]["items"]
track_list = []
for track in tracks:
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    track_list.append(f"{track_name} - {artist_name}")

# print the list of track names and artist names

for item in track_list:
    print(item)
# List to be exported to file
links_export = []
with open("songs_links_temp.txt", "r") as f:
    existing_links = f.read().splitlines()

for track in track_list:
    if any(track in link for link in existing_links):
        # if the track is already in the file, extract the link and add it to link_export
        for link in existing_links:
            if track in link:
                song_link = link.split(": ")[1]
                links_export.append(song_link)
                print(f"{track}: {song_link} (already in file)")
                break
    else:
        # if the track is not in the file, run the query and write the link to the file
        query = f"{track} lyrics"
        video_links = search_youtube(query)
        if video_links:
            song_link = video_links[0]
            links_export.append(song_link)
            print(f"{track}: {song_link}")
            with open("songs_links_temp.txt", "a") as f:
                f.write(f"{track}: {song_link}\n")
