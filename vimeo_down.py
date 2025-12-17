import yt_dlp

def download_vimeo_video(url, output_path='./downloads/%(title)s.%(ext)s'):
    """
    Downloads a Vimeo video using yt-dlp.
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', # Prioritizes mp4 format
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'noplaylist': True, # Ensures only the single video is downloaded
        'verbose': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage:
video_url = "https://vimeo.com/1147368922?share=copy&fl=sv&fe=ci" # Replace with the actual Vimeo URL
download_vimeo_video(video_url)
