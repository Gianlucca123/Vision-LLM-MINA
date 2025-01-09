from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Load descriptions of video from .txt file
    with open("interface/static/descriptions.txt", "r") as file:
        descriptions_text = file.read()
    
    return render_template("index.html", video_url=url_for("static", filename="video.mp4"), descriptions_text=descriptions_text)

if __name__ == "__main__":
    app.run(debug=True)
