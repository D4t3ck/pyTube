# YouTube Video Downloader with yt-dlp

This is a Python script for downloading YouTube videos using the yt-dlp library. It supports downloading the best available video and audio quality, merging them using ffmpeg, and saving them to your Desktop.

## Features

- Downloads the best video and audio quality from YouTube.
- Merges video and audio using FFmpeg.
- Saves the downloaded files directly to the user's Desktop.
- Simple and user-friendly input for YouTube URLs.

## Prerequisites

1. **Python 3.7 or higher**

   - Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **yt-dlp**

   - Install the `yt-dlp` library by running:

     ```bash
     pip install yt-dlp
     ```

3. **FFmpeg**

   - Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/).
   - Extract the FFmpeg folder and ensure the `ffmpeg.exe` file is located in the `bin` directory.
   - Note the path to the `ffmpeg.exe` file (e.g., `C:/Users/yourusername/ffmpeg/bin/ffmpeg.exe`).

## How to Use

1. **Clone or Download the Repository**

   - Clone this repository using Git:

     ```bash
     git clone https://github.com/yourusername/yt-downloader.git
     ```

   - Alternatively, you can download the repository as a ZIP file and extract it.

2. **Update the FFmpeg Path**

   - Open the Python script (`youtube_downloader.py`) in a text editor.
   - Update the `ffmpeg_path` variable with the full path to your `ffmpeg.exe` file.

     Example:

     ```python
     ffmpeg_path = r'C:/Users/yourusername/ffmpeg/bin/ffmpeg.exe'
     ```

3. **Run the Script**

   - Open a terminal or command prompt in the script's directory.
   - Run the script using:

     ```bash
     python youtube_downloader.py
     ```

4. **Input the YouTube URL**

   - Enter the YouTube video URL when prompted.
   - The video will be downloaded to your Desktop.

## Key Highlights

- The `ffmpeg_location` parameter ensures that yt-dlp uses the correct FFmpeg binary.
- The `outtmpl` parameter saves the downloaded file with the video's title as the filename, ensuring user-friendly naming.

## Troubleshooting

### Common Errors

1. **FFmpeg not found**

    - Ensure the `ffmpeg_path` variable points to the correct location of `ffmpeg.exe`.

2. **yt-dlp download issues**

    - Ensure `yt-dlp` is properly installed by running:

      ```bash
      pip show yt-dlp
      ```

3. **Permission errors**

    - Run the script with administrator privileges if needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions and suggestions are welcome! Feel free to fork this repository and submit pull requests.

---

Happy downloading! 🎥🎶
