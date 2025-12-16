import yt_dlp
def download_with_yt_dlp(video_url):
    ydl_opts = {
        'format': 'best',  # Selects the best available format
        'noplaylist': True, # Ensure only the single video is downloaded
        'progress_hooks': [my_hook], # Optional: add a hook to monitor progress
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {video_url}")
            ydl.download([video_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error has occurred: {e}")

# Optional: A simple progress hook function
def my_hook(d):
    if d['status'] == 'finished':
        print(f"\nDone downloading {d['filename']}")
    elif d['status'] == 'downloading':
        print(f"Downloading... {d['_percent_str']} at {d['_speed_str']} ETA {d['_eta_str']}", end='\r')

# Request the video URL from the user
video_url = input("Please enter the full YouTube video URL: ")
# Run the download function
download_with_yt_dlp(video_url)
