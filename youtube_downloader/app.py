from flask import Flask, render_template, request, flash, send_from_directory
import yt_dlp
import os
import uuid

app = Flask(__name__)
app.secret_key = 'secret'

FFMPEG_PATH = "C:/ffmpeg/bin/ffmpeg.exe"
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_video(url, audio_only=False):
    video_id = str(uuid.uuid4())[:8] # short unique ID
    outtmpl = os.path.join(DOWNLOAD_FOLDER, f"%(title)s_{video_id}.%(ext)s")

    ydl_opts = {
        'ffmpeg_location': FFMPEG_PATH,
        'format': 'bestaudio/best' if audio_only else 'best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp4',
            'preferredquality': '192',
        }] if audio_only else [],
        'outtmpl': outtmpl,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        ext = 'mp4' if audio_only else info['ext']
        filename = f"{info['title']}_{video_id}.{ext}"
        return filename # Just the name, not full path.
    

@app.route("/", methods=["GET", "POST"])
def index():
    video_file = None
    if request.method == "POST":
        url = request.form.get("url").strip()
        audio_only = request.form.get("audio_only") == "on"

        if not url:
            flash("Please enter a valid YouTube URL.", "success")
        else:
            try:
                filename = download_video(url, audio_only)
                flash("Download completed successfully!", "success")
                if not audio_only:
                    video_file = filename
            except Exception as e:
                flash(f"Error during download: {e}", "danger")

    return render_template("index.html", video_file=video_file)


@app.route("/video/<filename>")
def video(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)

