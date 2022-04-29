import os 
import subprocess
from pathlib import Path
from pytube import YouTube

while 1 :
    link = input("Enter the link: ")
    yt = YouTube(link)
    downloads_path = str(Path.home() / "Downloads")
    print("Found: ", yt.title)

    #choice = input("Download audio(1) or video(2): ")
    choice = '1'
    if choice == '1':
        ys = yt.streams.get_by_itag('140')
        ys.download(downloads_path)
        path = ys.default_filename
        convpath = yt.title + ".mp3"

        subprocess.run([
            'ffmpeg',
            '-i', os.path.join(downloads_path, path),
            os.path.join(downloads_path, convpath)
        ])
        os.remove(os.path.join(downloads_path, path))
        print("Downloaded: ", convpath)
    else:
        video = yt.streams.filter(only_video=True)
        print("---Available video---")
        print(video)