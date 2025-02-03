from flask import Flask, render_template, request, jsonify
from utils.utils import compute_video_metadata, compute_transcription

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/load-video', methods=["GET"])
def load_video():
    video_file_name = request.args.get('video_file_name')
    return jsonify(compute_video_metadata(video_file_name))

@app.route('/start-transcription', methods=["GET"])
def start_transcription():
    video_file_name = request.args.get('video_file_name')
    frame_rate = request.args.get('frame_rate')
    success = compute_transcription(video_file_name, frame_rate)
    return jsonify({'success': success})

if __name__ == '__main__':
    app.run(debug=True)