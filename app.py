from flask import Flask, render_template, send_from_directory
import os

print("You can use ur ip and open a port on 5000 for a real webserver")

app = Flask(__name__)

VIDEO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")

def load_videos():
    if not os.path.exists(VIDEO_DIR):
        return []
    return [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith(".mp4")]

@app.route("/")
def intro():
    # Zeige die Intro-Seite mit Animation
    return render_template("index.html")

@app.route("/videos")
def videos():
    vids = load_videos()
    return render_template("videos.html", videos=vids)

@app.route("/video/<filename>")
def serve_video(filename):
    if ".." in filename or filename.startswith("/"):
        return "Ungültiger Dateiname", 400
    return send_from_directory(VIDEO_DIR, filename)

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
