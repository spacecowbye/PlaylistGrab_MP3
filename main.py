import pytube
import os
import GetSongsFromSpotify
import re

# set the YouTube video URL
links = GetSongsFromSpotify.links_export

def download_audio(links):
    for link in links:
        for link in links:
            # create a YouTube object and get the audio stream
            try:
                yt = pytube.YouTube(link)
                audio = yt.streams.filter(only_audio=True).first()

                # clean up the filename
                filename = re.sub(r'[^\w\-_. ]', '', yt.title)
                filename = filename.replace(' ', '_') + '.mp3'

                # download the audio stream and save it as an MP3 file
                audio.download(output_path=os.getcwd(), filename=filename)

                print(f"{yt.title} downloaded successfully!")
            except pytube.exceptions.VideoUnavailable:
                print(f"{link} is unavailable for streaming.")
            except Exception as e:
                print(f"An error occurred while downloading {link}: {e}")


download_audio(links)