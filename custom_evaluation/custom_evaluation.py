import cv2
import numpy as np


def custom_evaluation(
    video_path,
    ground_truth_path,
    model_path,
    video_model,
    fps,
):
    """
    @brief Custom evaluation function for video processing models.
    This function evaluates a video processing model by applying various modifications to the input video and comparing the model's output to a ground truth summary using Jaccard similarity.
    @param video_path Path to the input video file.
    @param ground_truth_path Path to the ground truth summary file.
    @param model_path Path to the model file.
    @param video_model Boolean indicating whether the model processes the whole video at once (True) or frame by frame (False).
    @param fps Frames per second to process the video. If fps is 0, the original fps of the video is used.
    @return None
    """

    # Open the video
    video = cv2.VideoCapture(video_path)
    input_fps = video.get(cv2.CAP_PROP_FPS)

    # Load the model
    # TO BE DONE

    # Define modifications to the video
    # (e.g. resize, blur, noise, black and white, different color space, distortion, etc.)
    videos_quality = ["1080p", "720p", "480p", "240p"]
    videos_modifications = [
        "original",
        "blur",
        "noise",
        "black_and_white",
        "distortion",
        "different_color_space",
    ]

    # Run the model on the videos
    for quality in videos_quality:
        for modification in videos_modifications:
            # Read the video frame by frame (at a given fps) if video_model is False and compute the model output
            if not video_model:
                frame_counter = 0
                while video.isOpened():
                    ret, frame = video.read()
                    if not ret:
                        break

                    # Skip frames if the fps is too high
                    frame_counter += 1
                    if fps > 0:
                        if (frame_counter - 1) % (input_fps / fps) != 0:
                            continue

                    # Apply the modifications to the frame
                    resized_frame = reduce_frame_quality(frame, quality)
                    modified_frame = apply_modification(resized_frame, modification)

                    # Run the model on the modified frame
                    # TO BE DONE

                    # Store the model output
                    # TO BE DONE

            else:
                # The model takes the whole video as input
                # TO BE DONE
                pass

            pass

    # Open & read the ground truth summary
    with open(ground_truth_path, "r") as file:
        ground_truth = file.readlines()

    # Compare the model output with the ground truth using Jaccard similarity
    # TO BE DONE

    # Display the results
    # TO BE DONE

    pass


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
    elif "720p":
        target_resolution = (1280, 720)
    elif "480p":
        target_resolution = (854, 480)
    elif "240p":
        target_resolution = (426, 240)
    else:
        raise ValueError(
            "Invalid target resolution. Please choose between 1080p, 720p, 480p, or 240p."
        )

    # Define 1080p resolution
    target_resolution = (1920, 1080)

    # Resize the frame to 1080p
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
        modified_frame = cv2.GaussianBlur(resized_frame, (5, 5), 0)
    elif modification == "noise":
        noise = np.random.normal(0, 1, resized_frame.shape)
        modified_frame = resized_frame + noise
    elif modification == "black_and_white":
        modified_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        # Verify if the shape of the modified frame is compatible with the model
    elif modification == "distortion":
        # Define the distortion matrix
        distortion_matrix = np.float32([[1, 0.2, 0], [0.2, 1, 0]])
        modified_frame = cv2.warpAffine(
            resized_frame, distortion_matrix, resized_frame.shape[:2]
        )
    elif modification == "different_color_space":
        modified_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)
        # Verify if the modified frame is different from the original frame
    elif modification == "original":
        modified_frame = resized_frame
    else:
        raise ValueError(
            "Invalid modification. Please choose between blur, noise, black_and_white, distortion, or different_color_space."
        )
    return modified_frame
