import yt_dlp
url = input("enter your youtube video link : ")
ydl_opts = {
    'format' : 'best', 'outtmpl' : '%(title)s.%(ext)s'
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("download completed")