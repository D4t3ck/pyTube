#YouTube Video Downloader with yt-dlp

This is a Python script for downloading YouTube videos using the yt-dlp library. It supports downloading the best available video and audio quality, merging them using ffmpeg, and saving them to your Desktop.

#Features

Downloads the best video and audio quality from YouTube.

Merges video and audio using FFmpeg.

Saves the downloaded files directly to the user's Desktop.

Simple and user-friendly input for YouTube URLs.

#Prerequisites

Python 3.7 or higher

Make sure Python is installed on your system. You can download it from python.org.

yt-dlp

Install the yt-dlp library by running:

pip install yt-dlp

FFmpeg

Download FFmpeg from ffmpeg.org.

Extract the FFmpeg folder and ensure the ffmpeg.exe file is located in the bin directory.

Note the path to the ffmpeg.exe file (e.g., C:/Users/yourusername/ffmpeg/bin/ffmpeg.exe).

#How to Use

Clone or Download the Repository

Clone this repository using Git:

git clone https://github.com/yourusername/yt-downloader.git

Alternatively, you can download the repository as a ZIP file and extract it.

Update the ffmpeg Path

Open the Python script (youtube_downloader.py) in a text editor.

Update the ffmpeg_path variable with the full path to your ffmpeg.exe file.

Example:

ffmpeg_path = r'C:/Users/yourusername/ffmpeg/bin/ffmpeg.exe'

Run the Script

Open a terminal or command prompt in the script's directory.

Run the script using:

python youtube_downloader.py

Input the YouTube URL

Enter the YouTube video URL when prompted.

The video will be downloaded to your Desktop.


#Key Highlights

The ffmpeg_location parameter ensures that yt-dlp uses the correct FFmpeg binary.

The outtmpl parameter saves the downloaded file with the video's title as the filename, ensuring user-friendly naming.

#Troubleshooting

Common Errors

FFmpeg not found

Ensure the ffmpeg_path variable points to the correct location of ffmpeg.exe.

yt-dlp download issues

Ensure yt-dlp is properly installed by running:

pip show yt-dlp

Permission errors

Run the script with administrator privileges if needed.

#License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributions

Contributions and suggestions are welcome! Feel free to fork this repository and submit pull requests.

Happy downloading! 🎥🎶

