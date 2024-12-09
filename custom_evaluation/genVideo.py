from utils.degraded_videos import degraded_videos
import argparse


def gen_video(video_path, output_folder_path, output_fps):
    """
    @brief Generate the degraded videos for the custom evaluation.
    This function parses the command-line arguments to get the path to the video file
    and the output directory for the degraded videos. It then calls the degraded_videos
    function with the provided video path.
    @param video_path Path to the video file.
    @param output_path Path to the output directory for the degraded videos.
    """

    degraded_videos(video_path, output_folder_path, output_fps)


""" if __name__ == "__main__":
    main() """

# e.g.
# python .\genVideo.py --video_path "data/input/cam-philippines-5min.mp4" --output_folder_path "data/output/video_degraded/" --output_fps 1
