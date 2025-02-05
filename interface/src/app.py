from flask import Flask, render_template, request, jsonify, Response
from utils.utils import (
    compute_video_metadata,
    compute_transcription,
    test_yield,
    retrieve_video_file,
)

app = Flask(__name__)
app.config["video_folder_path"] = "interface/data/videos/"


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Load video route
@app.route("/load-video", methods=["POST"])
def load_video():
    """
    @brief Handles the upload of a video file and saves it on the server.
    This function checks if a video file is included in the request, validates the file,
    saves it to a specified folder on the server, and computes metadata for the video.
    @return A JSON response with a success message and video metadata if the file is successfully saved,
            or an error message if the file is not included, not selected, or fails to save.
    """

    if "video_file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    video_file = request.files["video_file"]

    if video_file.filename == "":
        return jsonify({"message": "No selected file"}), 400

    # video folder path on the server
    video_folder_path = app.config["video_folder_path"]

    # Save the video file on the server
    if not retrieve_video_file(video_file, video_folder_path):
        return jsonify(
            {"message": f"Failed to save video file: {video_file.filename}"}
        ), 500

    return jsonify(compute_video_metadata(video_file.filename, video_folder_path))


# Start transcription route
@app.route("/start-transcription", methods=["GET"])
def start_transcription():
    """
    @brief Starts the transcription process for a given video file.
    This function retrieves the video file name, frame rate, prompt, and maximum token length from the request arguments.
    It then calls the compute_transcription function with these parameters and returns the result as a streaming response.
    @return Response object with the transcription result in "text/event-stream" MIME type.
    @param video_file_name The name of the video file to be transcribed.
    @param frame_rate The frame rate at which the video should be processed.
    @param prompt The prompt to guide the transcription process.
    @param max_token_length The maximum length of tokens for the transcription.
    @param video_folder_path The path to the folder containing the video files.
    """

    video_file_name = request.args.get("video_file_name")
    frame_rate = float(request.args.get("frame_rate"))
    prompt = request.args.get("prompt")
    max_token_length = int(request.args.get("max_token_length"))
    video_folder_path = app.config["video_folder_path"]
    return Response(
        compute_transcription(
            video_file_name, frame_rate, prompt, max_token_length, video_folder_path
        ),
        mimetype="text/event-stream",
    )


if __name__ == "__main__":
    app.run(debug=True)
