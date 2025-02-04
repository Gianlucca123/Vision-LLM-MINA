import cv2
import os
import math
from utils.callModel import get_answer_InternVL2_1B
from time import sleep

def compute_video_metadata(video_file_name):
    """
    Compute metadata for a given video file.
    This function opens a video file using OpenCV, calculates the total number of frames,
    the frames per second (fps), and the duration of the video in seconds.
    @param path: The file path to the video.
    @type path: str
    @return: A dictionary containing the frame count, fps, and duration of the video.
    @rtype: dict
    @raises ValueError: If the video file cannot be opened.
    """

    # open the video with OpenCV
    path = f"interface/data/videos/{video_file_name}"
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
    return {
        'frame_count': frame_count,
        'fps': fps,
        'duration': duration
    }


def compute_transcription(video_file_name, frame_rate):
    # open the video with OpenCV
    path = f"interface/data/videos/{video_file_name}"
    cap = cv2.VideoCapture(path)
    
    if not cap.isOpened():
        raise ValueError(f"Unable to open video file: {path}")

    # compute the frame gap
    frame_rate = int(frame_rate)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_gap = math.floor(60 / (fps*frame_rate))

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

    # get the answer for the InternVL2_1B model
    #return get_answer_InternVL2_1B(cached_images_dir)
    return test_yield()


def test_yield():
    cache_path = "interface/data/cache"
    for i, name in enumerate(os.listdir(cache_path)):
        path = os.path.join(cache_path, name)
        sleep(1)

        # remove the .jpg from name and remove the leading zeros (except if the name is 0)
        name = name[:-4].lstrip("0")
        if name == "":
            name = "0"

        yield f"data: {dict(frame_id = name, answer = "This is the answer number " + str(i))}\n\n"