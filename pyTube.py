import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Specify the path to ffmpeg.exe (ensure the path is correct)
ffmpeg_path = r'C:/Users/danie/ffmpeg/bin/ffmpeg.exe'

# Function to handle the download process
def download_video():
    # Get the URL entered by the user
    url = url_entry.get()
    
    if not url or url == "URL":  # Check if URL field is empty or contains placeholder text
        messagebox.showerror("Input Error", "Please enter a valid YouTube URL.")
        return
    
    # Get the download folder path from the input field
    download_folder = folder_path.get()
    
    if not download_folder or download_folder == "Download Folder":  # Check for placeholder text
        messagebox.showerror("Input Error", "Please select a download folder.")
        return
    
    # Configure yt-dlp options to use FFmpeg and set the download location to the chosen folder
    ydl_opts = {
        'ffmpeg_location': ffmpeg_path,  # Full path to ffmpeg.exe
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio quality
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save location and filename
    }

    # Try downloading the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Download Complete", f"The video has been saved to: {download_folder}")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {e}")

# Function to choose the download folder
def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

# Function to clear placeholder text when the user clicks into the input fields
def clear_placeholder(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)

# Function to add placeholder text back when the input field is empty
def add_placeholder(event, entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Set window size
root.geometry("500x300")

# Create and place the URL input label
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

# Create and place the URL input field with placeholder text
url_entry = tk.Entry(root, width=40)
url_entry.insert(0, "URL")  # Placeholder text
url_entry.pack(pady=5)
url_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, url_entry, "URL"))
url_entry.bind("<FocusOut>", lambda event: add_placeholder(event, url_entry, "URL"))

# Create and place the "Choose Folder" button
folder_button = tk.Button(root, text="Browse", command=choose_folder)
folder_button.pack(pady=5)

# Create a variable to store the selected folder path
folder_path = tk.StringVar()

# Create and place the folder input field to display the selected folder path with placeholder text
folder_entry = tk.Entry(root, textvariable=folder_path, width=40)
folder_entry.insert(0, "Download Folder")  # Placeholder text
folder_entry.pack(pady=5)
folder_entry.bind("<FocusIn>", lambda event: clear_placeholder(event, folder_entry, "Download Folder"))
folder_entry.bind("<FocusOut>", lambda event: add_placeholder(event, folder_entry, "Download Folder"))

# Create and place the download button with green background
download_button = tk.Button(root, text="Download Video", command=download_video, bg="green", fg="white")
download_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
