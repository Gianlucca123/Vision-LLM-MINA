from frames_video import frame_video
from utils.degraded_videos import degraded_videos
import argparse

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
        default="../data/output/videos_degraded",
        help="Name of the output directory for the degraded videos",
    )
    parser.add_argument(
        "--frames_output",
        default="../data/output/frames",
        help="Name of the output directory for the frames",
    )
    parser.add_argument(
        "--output_fps",
        type=int,
        default=0,
        help="Output fps for the degraded videos, default is the same as the input video.",
    )
    parser.add_argument(
        "--time", 
        nargs='+', 
        help="List of time strings in format 'MM:SS'"
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
        help="modifications for the video"
    )

    args = parser.parse_args()

    degraded_videos(args.video_path, args.videos_output, args.output_fps, args.video_quality, args.video_modifications)

    frame_video(args.videos_output, args.time, args.video_quality, args.video_modifications, args.frames_output)

if __name__ == "__main__":
    main()
