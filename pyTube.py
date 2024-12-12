import yt_dlp
import os

# Specify the path to ffmpeg.exe (ensure the path is correct)
ffmpeg_path = r'C:/Users/danie/ffmpeg/bin/ffmpeg.exe'

# Path to the Desktop (platform-independent)
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Configure yt-dlp options to use FFmpeg and set the download location to the Desktop
ydl_opts = {
    'ffmpeg_location': ffmpeg_path,  # Full path to ffmpeg.exe
    'format': 'bestvideo+bestaudio/best',  # Download the best video and audio quality
    'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),  # Save location and filename
}

# Prompt the user to input the YouTube URL
url = input("Please enter the YouTube URL: ")

# Download the video
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Download complete! The video has been saved to the Desktop: {desktop_path}")
except Exception as e:
    print(f"An error occurred: {e}")
