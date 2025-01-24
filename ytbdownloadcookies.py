import subprocess
import yt_dlp

def check_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg đã được cài đặt.")
        return True
    except FileNotFoundError:
        print("FFmpeg chưa được cài đặt. Vui lòng cài đặt và thử lại.")
        return False

def download_youtube_video(url):
    if not check_ffmpeg_installed():
        return
    try:
        # Cấu hình yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Tải chất lượng tốt nhất
            'outtmpl': '%(title)s.%(ext)s',       # Tên file theo tiêu đề video
            'merge_output_format': 'mp4',        # Lưu file dưới định dạng MP4
            'noplaylist': True,                  # Chỉ tải một video, không tải playlist
            'cookiefile': 'cookies2.txt',         # Sử dụng cookies từ file cookies.txt
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',   # Dùng bộ chuyển đổi video
                'preferedformat': 'mp4'         # Chuyển đổi sang MP4
            }],
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        # Sử dụng yt-dlp để tải video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Đang tải video từ URL: {url}")
            ydl.download([url])
            print("Tải xuống thành công dưới định dạng MP4!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# URL video YouTube cần tải
video_url = input("Nhập URL video YouTube: ")
download_youtube_video(video_url)