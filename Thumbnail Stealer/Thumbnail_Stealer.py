import re
from pathlib import Path
import pyfiglet  # pip install pyfiglet

def download_thumbnail(video_url, output_filename="thumbnail.jpg"):
    video_id = extract_video_id(video_url)
    if not video_id:
        print("❌ Invalid YouTube URL.")
        return

    resolutions = ["maxresdefault", "sddefault", "hqdefault", "mqdefault", "default"]
    
    for resolution in resolutions:
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/{resolution}.jpg"
        if try_download(thumbnail_url, output_filename):
            print(f"✅ Downloaded {resolution} thumbnail as {output_filename}")
            return
    
    print("⚠️ No valid thumbnail found.")

def extract_video_id(url: str):
    """Extracts a YouTube video ID from various URL formats (watch, share, embed, shorts)."""
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",            # watch?v=, embed/, /v/
        r"youtu\.be\/([0-9A-Za-z_-]{11})",          # youtu.be/<id>
        r"youtube\.com\/shorts\/([0-9A-Za-z_-]{11})" # shorts/<id>
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def try_download(url: str, output_filename: str, min_size=2000):
    """Attempts to download a thumbnail. Returns True if successful and not a tiny placeholder."""
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            # Check content length (skip tiny placeholder images)
            if int(response.headers.get("Content-Length", 0)) < min_size:
                return False
            
            output_path = Path(output_filename)
            with open(output_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return True
    except Exception as e:
        print(f"❌ Error downloading: {e}")
    return False

# Example usage
if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("YT Thumbnail Grabber - Made By Exploits")
    print(ascii_banner)
    video_url = input("Enter the YouTube video URL: ")
    download_thumbnail(video_url, "thumbnail.jpg")