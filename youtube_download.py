import yt_dlp
import os

# 🔹 你要下載的 YouTube 影片網址
video_url = "https://www.youtube.com/watch?v=ACo60qnd_Lc"  # 請更換為你的 YouTube 影片網址

# 🔹 設定 yt-dlp 參數
ydl_opts = {
    'format': 'bestaudio/best',  # 下載最佳音質
    'outtmpl': '%(title)s.%(ext)s',  # 檔案命名（影片標題）
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # 轉換音訊
        'preferredcodec': 'mp3',  # 設定轉換為 MP3
        'preferredquality': '192',  # 設定音訊品質（192kbps）
    }],
}

# 🔹 執行 yt-dlp 下載
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("✅ 下載完成！MP3 檔案已儲存於當前資料夾。")

# 🔹 確認 MP3 檔案名稱（避免找不到檔案）
mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]
if mp3_files:
    print(f"🎵 下載的 MP3 檔案名稱: {mp3_files[0]}")
else:
    print("❌ 未找到 MP3 檔案，請確認下載是否成功！")
