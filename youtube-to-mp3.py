import youtube_dl
import shutil
import re


def run():
    video_url = input('Enter the YouTube URL. ')
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
    name = re.sub(r'[^\w\s]', '', video_info.get('title'))
    filename = f"{name}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    shutil.move(filename, r'C:\Users\ChonNgo\songs')


if __name__ == '__main__':
    run()

