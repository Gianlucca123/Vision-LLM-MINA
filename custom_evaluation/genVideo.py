from degraded_videos import degraded_videos
import argparse


def main():
    """
    @brief Generate the degraded videos for the custom evaluation.
    This function parses the command-line arguments to get the path to the video file
    and the output directory for the degraded videos. It then calls the degraded_videos
    function with the provided video path.
    @param video_path Path to the video file.
    @param output_path Path to the output directory for the degraded videos.
    """

    parser = argparse.ArgumentParser(
        description="Generate the degraded videos for the custom evaluation."
    )
    parser.add_argument(
        "--video_path",
        type=str,
        default="data/input/video_test.mp4",
        help="Path to the video file.",
    )
    parser.add_argument(
        "--output_folder_path",
        type=str,
        default="data/output/",
        help="Path to the output directory for the degraded videos",
    )
    parser.add_argument(
        "--output_fps",
        type=int,
        default=0,
        help="Output fps for the degraded videos, default is the same as the input video.",
    )

    args = parser.parse_args()
    degraded_videos(args.video_path, args.output_folder_path, args.output_fps)


if __name__ == "__main__":
    main()

# e.g.
# python .\genVideo.py --video_path "data/input/cam-philippines-5min.mp4" --output_folder_path "data/output/" --output_fps 1
