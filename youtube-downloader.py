import yt_dlp

url = input("enter your youtube video link : ")

ydl_opts = {
    'format': 'bv*+ba/b',
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
    'extractor_args': {
        'youtube': {
            'player_client': ['android', 'web']
        }
    }
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("download completed")