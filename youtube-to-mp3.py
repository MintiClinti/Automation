import youtube_dl
import shutil
from slugify import slugify


def run():
    video_url = input('Enter the YouTube URL. ')
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    name = slugify(video_info['title'])
    filename = f"{name}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    shutil.move(filename, r'C:\Users\ChonNgo\songs')


if __name__ == '__main__':
    run()
