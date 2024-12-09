from frames_video import frame_video
from genVideo import gen_video

import argparse
import os
import cv2

def main():
    parser = argparse.ArgumentParser(
        description="Generate the degraded videos for the custom evaluation."
    )
    parser.add_argument(
        "--video_path",
        type=str,
        help="Path to the video file.",
    )
    """ parser.add_argument(
        "--output_folder_name",
        type=str,
        default="Videos_degraded",
        help="Name of the output directory for the degraded videos",
    ) """
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

    args = parser.parse_args()

    output_folder_name = "videos_degraded"

    gen_video(args.video_path, output_folder_name, args.output_fps)

    frame_video(output_folder_name, args.time)


    


if __name__ == "__main__":
    main()
