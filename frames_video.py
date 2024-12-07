"""
/**
 * @file python frames_video.py path_video times_in_format_MM:SS
 * Ex: python frames_video.py cam-philippines-5min.mp4 00:23 00:55 01:01 01:23 02:34 02:55 03:15 03:44 04:02 04:45
 * @brief Python script to get the frames of a video at the especific time given.
 */
"""

import argparse
import os
import cv2

def list_of_times_seconds(list_times, time_seconds):
    """
    /**
     * @brief Converts a list of time strings (MM:SS) to total seconds.
     * 
     * @param list_times List of time strings in MM:SS format.
     * @param time_seconds List to store the resulting time values in seconds.
     */
    """
    for time in list_times:
        minutes, seconds = map(int, time.split(":"))
        time_seconds.append(minutes * 60 + seconds)


def getFrame(sec, video, i, time_min):
    """
    /**
     * @brief Captures a video frame at a specified time and saves it as a PNG file. Create a txt file with the same name of the frame.
     * 
     * @param sec The time in seconds where the frame should be captured.
     * @param video The video file object to capture frames from.
     * @param i The frame index for naming the output file.
     * @param time_min The original time string (MM:SS) for naming the output file.
     * @return True if the frame was successfully captured, False otherwise.
     */
    """
    video.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = video.read()
    if hasFrames:
        cv2.imwrite("frames/" + "frame" + str(i) + "_" + time_min + ".png", image) 
        file = open("frames/" + "frame" + str(i) + "_" + time_min + ".txt", "w") 
        file.close()
    return hasFrames


def main():
    """
     * @brief Main function to process video and extract frames at specified times.
     * 
     * Parses command-line arguments to get the video path and time list, then processes the video to extract
     * and save frames corresponding to each specified time.
    """

    # Deal with arguments in the command line 
    parser = argparse.ArgumentParser(description="Process a video path and time arguments.")
    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument("time", nargs='+', help="List of time strings in format 'MM:SS'")
    args = parser.parse_args()

    times_sec = []

    list_of_times_seconds(args.time, times_sec)

    video = cv2.VideoCapture(args.video_path)

    # Create a directory called "frames" if it does not already exist
    try:
        directory_name = "frames"
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

    # Pass each time to the function getFrame 
    for i, sec in enumerate(times_sec):
        if getFrame(sec, video, i + 1, args.time[i]):
            print(f"Frame {args.time[i]} saved successfully.")
        else:
            print(f"Time {args.time[i]} does not exist in the video.")


if __name__ == "__main__":
    main()
