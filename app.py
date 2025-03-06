from flask import Flask, render_template, request, send_from_directory
import yt_dlp
import os

app = Flask(__name__)

# 確保下載資料夾存在
DOWNLOAD_FOLDER = "static/downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# 🔹 首頁（顯示輸入框）
@app.route('/')
def index():
    return render_template('index.html')

# 🔹 處理 YouTube 下載請求
@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    
    # 設定 yt-dlp 參數
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',  # 存入指定資料夾
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # 執行下載
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        filename = ydl.prepare_filename(info_dict)
        mp3_filename = filename.rsplit(".", 1)[0] + ".mp3"

    mp3_basename = os.path.basename(mp3_filename)  # 取得純檔名
    return render_template('index.html', download_link=mp3_basename)

# 🔹 提供 MP3 檔案下載
@app.route('/static/downloads/<filename>')
def serve_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

"""
if __name__ == '__main__':
    app.run(debug=True)
"""

if name == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)