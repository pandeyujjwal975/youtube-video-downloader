 # YouTube Video Downloader 🎥

A minimal, efficient Python script to download YouTube videos directly to your local machine. Built using the powerful `yt-dlp` library.

---

## 📖 Explanation
This script uses the `yt-dlp` library, which is a feature-rich fork of the original `youtube-dl`. 

### How the code works:
* **`yt_dlp.YoutubeDL(ydl_opts)`**: Initializes the downloader with a dictionary of settings.
* **`'format': 'best'`**: Instructs the script to look for a single file that contains both high-quality video and audio.
* **`'outtmpl': '%(title)s.%(ext)s'`**: This is the output template. It dynamically names the file based on the YouTube video title rather than a random string of characters.
* **The Context Manager (`with ... as ydl`)**: This ensures that even if the download fails or is interrupted, the program closes the connection and cleans up temporary files properly.

---

## 🛠 Prerequisites
Before running the script, you must have the following:

1.  **Python 3.7+**
2.  **yt-dlp library**: The engine that handles the extraction.
3.  **FFmpeg (Recommended)**: While not strictly required for the "best" single-file format, it is required if you want to download 4K video or extract high-quality MP3s.

---

## 📦 Installation

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

```

2. **Install the required library:**
```bash
pip install yt-dlp

```



---

## 🚀 How to Use

1. **Run the script:**
```bash
python main.py

```


2. **Enter the URL:** When prompted, paste the full YouTube link (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
3. **Wait for completion:** The script will display the download progress. Once finished, you will see the message: `download completed`.
4. **Find your file:** The video will be saved in the **same folder** where the script is located.

---

## ⚙️ Customization

If you want to change how the script behaves, you can modify the `ydl_opts` dictionary:

* **Change download folder:** Change `outtmpl` to `'Downloads/%(title)s.%(ext)s'` to save files in a folder named "Downloads".
* **Download Audio Only:** Change `'format': 'best'` to `'format': 'bestaudio/best'`.

---

## Author : Ujjwal Pandey, Github :  https://github.com/pandeyujjwal975

## 📜 License

This project is open-source. Feel free to fork, modify, and use it for your own purposes.


