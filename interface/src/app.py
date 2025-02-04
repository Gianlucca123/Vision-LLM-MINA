from flask import Flask, render_template, request, jsonify, Response
from utils.utils import compute_video_metadata, compute_transcription, test_yield

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
    prompt = request.args.get('prompt')
    max_token_length = request.args.get('max_token_length')
    return Response(compute_transcription(video_file_name, frame_rate, prompt, max_token_length), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)