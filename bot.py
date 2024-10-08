import os
import yt_dlp

def check_if_downloaded(url, log_file='downloaded_urls.txt'):
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            downloaded_urls = f.read().splitlines()
            if url in downloaded_urls:
                return True
    return False

def log_downloaded_url(url, log_file='downloaded_urls.txt'):
    with open(log_file, 'a') as f:
        f.write(url + '\n')

def find_ffmpeg():
    # Check for ffmpeg in the same directory as the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(current_dir, 'ffmpeg', 'bin', 'ffmpeg.exe')  # Adjust if necessary
    return ffmpeg_path if os.path.exists(ffmpeg_path) else None

def download_video(video_url):
    output_dir = 'hasil'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ffmpeg_location = find_ffmpeg()
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'ffmpeg_location': ffmpeg_location,  # Use the detected ffmpeg path
    }

    if check_if_downloaded(video_url):
        print("URL sudah diunduh sebelumnya. Menghindari pengunduhan ulang.")
    else:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        log_downloaded_url(video_url)

if __name__ == "__main__":
    video_url = input("Masukkan URL video Reels yang ingin diunduh: ")
    download_video(video_url)
