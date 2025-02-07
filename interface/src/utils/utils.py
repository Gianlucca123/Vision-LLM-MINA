import cv2
import os
import math
from utils.callModel import get_answer_InternVL2_1B
from time import sleep
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timezone
from utils.logs import define_log_file, write_logs
from utils.question_answering.Qwen25 import questionQwen, open_Qwen05, open_Qwen15, clean_cuda


def retrieve_video_file(video_file, video_folder_path):
    """
    @brief Save an uploaded video file to a specified folder on the server.
    @param video_file The video file object to be saved.
    @param video_folder_path The path to the folder where the video file should be saved.
    @return True if the file was successfully saved.
    This function secures the filename, creates the directory if it does not exist,
    and saves the video file to the specified folder path.
    """

    # Secure the filename
    video_file_name = secure_filename(video_file.filename)

    # Make directory if it doesn't exist
    if not os.path.exists(video_folder_path):
        os.makedirs(video_folder_path)

    # Save the file on the server
    file_path = os.path.join(video_folder_path, video_file_name)
    video_file.save(file_path)

    return True


def compute_video_metadata(video_file_name, video_folder_path):
    """
    @brief Computes metadata for a given video file.
    @param video_file_name The name of the video file.
    @param video_folder_path The path to the folder containing the video file.
    @return A dictionary containing the following metadata:
        - frame_count: The total number of frames in the video.
        - fps: The frames per second (FPS) of the video.
        - duration: The duration of the video in seconds.
    @throws ValueError If the video file cannot be opened.
    """

    # open the video with OpenCV
    path = os.path.join(video_folder_path, video_file_name)
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        raise ValueError(f"Unable to open video file: {path}")

    # compute the exact number of frames in the video
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

    # compute the duration of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = frame_count / fps

    # release the video capture object
    cap.release()

    # return the metadata
    return {"frame_count": frame_count, "fps": fps, "duration": duration}


def compute_transcription(
    video_file_name, frame_rate, prompt, max_token_length, video_folder_path
):
    """
    @brief Extracts frames from a video at a specified frame rate and processes them for transcription.
    This function opens a video file, extracts frames at a specified frame rate, saves them to a cache directory,
    and processes them for transcription using a specified model.
    @param video_file_name The name of the video file to process.
    @param frame_rate The rate at which frames should be extracted from the video (frames per minute).
    @param prompt The prompt to be used for the transcription model.
    @param max_token_length The maximum token length for the transcription model.
    @param video_folder_path The path to the folder containing the video file.
    @return The transcription result from the model.
    @throws ValueError If the video file cannot be opened.
    """
    # open the video with OpenCV
    path = os.path.join(video_folder_path, video_file_name)
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        raise ValueError(f"Unable to open video file: {path}")

    # compute the frame gap
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_gap = math.floor(fps * 60 / frame_rate)

    # create the cached images dir if it doesn't exist
    cached_images_dir = "interface/data/cache"
    if not os.path.exists(cached_images_dir):
        os.makedirs(cached_images_dir)

    # clear the cached images

    for file in os.listdir(cached_images_dir):
        os.remove(os.path.join(cached_images_dir, file))

    # get the images every frame_gap
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_gap == 0:
            frame_name = str(frame_count).zfill(10)
            cv2.imwrite(f"{cached_images_dir}/{frame_name}.jpg", frame)
        frame_count += 1

    # release the video capture object
    cap.release()

    # define a log file for the transcription
    log_file_path = define_log_file()

    # get the answer for the InternVL2_1B model
    answers = get_answer_InternVL2_1B(cached_images_dir, prompt, max_token_length, log_file_path, fps)
    #answers = test_yield(log_file_path, fps)

    return answers


# test function to simulate the yield
def test_yield(log_file_path, fps):
    """
    @brief Generator function that yields formatted data from files in a cache directory.
    This function iterates over files in the specified cache directory, processes each file name,
    and yields a formatted string containing the frame ID and a corresponding answer.
    @yield str Formatted string containing the frame ID and answer in the format:
               "data: {'frame_id': <name>, 'answer': <answer>}\n\n"
    """

    cache_path = "interface/data/cache"
    for i, name in enumerate(os.listdir(cache_path)):
        path = os.path.join(cache_path, name)
        sleep(1)

        # remove the .jpg from name and remove the leading zeros (except if the name is 0)
        name = name[:-4].lstrip("0")
        if name == "":
            name = "0"

        answer = 'This is the answer number "dlfk"  ' + str(i)
        answer = answer.replace("'", "").replace('"', "")

        # compute the timestamp using int(name)
        timestamp = int(name) / fps
        timestamp = str(
            datetime.fromtimestamp(timestamp, timezone.utc).strftime("%H:%M:%S")
        )

        # write the answer to the logs
        write_logs(answer, timestamp, name, log_file_path)

        yield f"data: {dict(frame_id=name, answer=answer)}\n\n"

def askQwen25(prompt):
    tokenizer,model=open_Qwen05()
    answer = questionQwen(prompt,tokenizer,model)
    clean_cuda(model, tokenizer)
    return answer