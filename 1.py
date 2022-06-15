from pytube import YouTube

DOWNLOAD_FOLDER = "/Users/xinapse/Desktop/TTS"

url = "hhttps://youtu.be/HHSUul3wJA4"

yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)