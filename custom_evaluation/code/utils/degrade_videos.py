import cv2
import numpy as np
from tqdm import tqdm
import os
import argparse


def degrade_videos(video_path, output_folder_path, output_fps, video_quality, video_modification):
    """
    Processes a video by applying various modifications and saves the modified videos to the specified output folder.
    @param video_path: Path to the input video file.
    @type video_path: str
    @param output_folder_path: Path to the folder where the modified videos will be saved.
    @type output_folder_path: str
    @param output_fps: Frames per second for the output video. If set to 0, the input video's fps will be used.
    @type output_fps: int
    @return: None
    """
    try:
        os.mkdir(output_folder_path)
        print(f"Directory '{output_folder_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{output_folder_path}' already exists.")

    # Run the model on the videos
    for quality in video_quality:
        for modification in video_modification:
            codec_defined = False
            # Define and display the output path
            output_path = os.path.join(output_folder_path, f"{quality}_{modification}.mp4")
            print(output_path)
            # Open the video
            video = cv2.VideoCapture(video_path)
            # Take in account the video's fps and total frames are not accurate, it's an estimation (See OpenCV documentation)
            input_fps = video.get(cv2.CAP_PROP_FPS)
            output_fps = input_fps if output_fps == 0 else output_fps
            total_frames_to_process = video.get(cv2.CAP_PROP_FRAME_COUNT) / (
                input_fps / output_fps
            )
            with tqdm(total=total_frames_to_process, desc="Video processing") as pbar:
                # Read the video frame by frame (at a given fps)
                frame_counter = 0
                while video.isOpened():
                    ret, frame = video.read()
                    if not ret:
                        break

                    # Skip frames if the fps from the original video is too high from the target fps
                    frame_counter += 1
                    if output_fps > 0:
                        if (frame_counter - 1) % int(input_fps / output_fps) != 0:
                            continue

                    # Apply the modifications to the frame
                    resized_frame = reduce_frame_quality(frame, quality)
                    modified_frame = apply_modification(resized_frame, modification)

                    # Define the codec and create VideoWriter object
                    if not codec_defined:
                        isColor = modification != "black_and_white"
                        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                        out = cv2.VideoWriter(
                            output_path,
                            fourcc,
                            output_fps,
                            (resized_frame.shape[1], resized_frame.shape[0]),
                            isColor,
                        )
                        codec_defined = True

                    # Write the modified frame to the output video
                    out.write(modified_frame)

                    # Update the progress bar
                    pbar.update(1)

                # Release the VideoWriter object if it was created
                if codec_defined:
                    out.release()


def reduce_frame_quality(frame, quality):
    """
    Reduces the quality of a given video frame to the specified resolution.
    @param frame: The input video frame to be resized.
    @param quality: The target resolution quality. Must be one of "1080p", "720p", "480p", or "240p".
    @return: The resized video frame.
    @raises ValueError: If the quality parameter is not one of the specified values.
    """

    if quality == "1080p":
        target_resolution = (1920, 1080)
    elif quality == "720p":
        target_resolution = (1280, 720)
    elif quality == "480p":
        target_resolution = (854, 480)
    elif quality == "240p":
        target_resolution = (426, 240)
    else:
        raise ValueError(
            "Invalid target resolution. Please choose between 1080p, 720p, 480p, or 240p."
        )

    # Resize the frame to a lower quality
    resized_frame = cv2.resize(frame, target_resolution, interpolation=cv2.INTER_AREA)

    return resized_frame


def apply_modification(resized_frame, modification):
    """
    @brief Applies a specified modification to the given frame.
    @param resized_frame The input frame to be modified. It should be a NumPy array representing an image.
    @param modification A string specifying the type of modification to apply.
                        Valid options are "blur", "noise", "black_and_white", "distortion", and "different_color_space".
    @return The modified frame after applying the specified modification.
    @throws ValueError If an invalid modification type is provided.
    The modifications are as follows:
    - "original": The original frame without any modifications (except quality resize).
    - "blur": Applies Gaussian blur to the frame.
    - "noise": Adds random noise to the frame.
    - "black_and_white": Converts the frame to grayscale.
    - "distortion": Applies a distortion effect to the frame.
    - "different_color_space": Converts the frame to HSV color space.
    """
    if modification == "blur":
        modified_frame = cv2.GaussianBlur(resized_frame, (0, 0), 5)
        # Take attention, the blur will be stronger on small resolutions videos as it computes the blur based on the neighbor pixels.

    elif modification == "noise":
        noise = np.random.normal(0, 1, resized_frame.shape).astype(np.uint8)
        modified_frame = cv2.addWeighted(resized_frame, 0.60, noise, 0.40, 0)

    elif modification == "black_and_white":
        modified_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    elif modification == "distortion":
        # Define the distortion matrix
        height, width = resized_frame.shape[:2]
        src_points = np.float32(
            [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]]
        )
        dst_points = np.float32(
            [
                [0, 0],
                [int(0.8 * (width - 1)), int(0.2 * height)],
                [int(0.2 * width), int(0.8 * (height - 1))],
                [width - 1, height - 1],
            ]
        )
        perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        modified_frame = cv2.warpPerspective(
            resized_frame, perspective_matrix, (width, height)
        )

    elif modification == "different_color_space":
        modified_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)

    elif modification == "no_modification":
        modified_frame = resized_frame

    else:
        raise ValueError(
            "Invalid modification. Please choose between blur, noise, black_and_white, distortion, different_color_space, or no_modification."
        )

    return modified_frame

def main():
    parser = argparse.ArgumentParser(
        description="Generate the degraded videos and take the frames based on the time given"
    )
    parser.add_argument(
        "--video_path",
        help="Path to the video file.",
    )
    parser.add_argument(
        "--videos_output",
        default="../data/videos_degraded",
        help="Name of the output directory for the degraded videos",
    )
    parser.add_argument(
        "--output_fps",
        type=int,
        default=0,
        help="Output fps for the degraded videos, default is the same as the input video.",
    )
    parser.add_argument(
        "--video_quality",
        nargs='+',
        choices=["1080p", "720p", "480p", "240p"],
        default=["1080p"],
        help="Define quality of the videos"
    )
    parser.add_argument(
        "--video_modifications",
        nargs='+',
        choices=[
        "no_modification",
        "blur",
        "noise",
        "black_and_white",
        "distortion",
        "different_color_space"
        ],
        default=["no_modification"],
        help="Define other modifications for the video"
    )

    args = parser.parse_args()

    degrade_videos(args.video_path, args.videos_output, args.output_fps, args.video_quality, args.video_modifications)

if __name__ == "__main__":
    main()

