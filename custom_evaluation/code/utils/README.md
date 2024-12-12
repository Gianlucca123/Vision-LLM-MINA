# Utils

## Overview

This README explains how to use the scripts `degrade_videos.py` and `frame_videos.py`. It is recommended to run these scripts from the folder `custom_evaluation`.

## Usage

### degrade_videos.py

Example command:
```bash
python3 utils/degrade_videos.py --video_path ../data/cam-philippines-5min.mp4 --output_fps 1 --video_quality 480p --video_modifications no_modification
```

#### Arguments

- `--video_path`
  - **Help**: Path to the video file.
  - **Explanation**: Specifies the path to the video. This argument is required for the script to run.

- `--videos_output`
  - **Default**: `../data/videos_degraded`
  - **Help**: Path to the folder containing the degraded videos.
  - **Explanation**: Specifies the output folder for degraded videos. This argument is optional.

- `--output_fps`
  - **Default**: `0`
  - **Help**: Output FPS for the degraded videos. Defaults to the same FPS as the input video.

- `--video_quality`
  - **Default**: `1080p`
  - **Choices**: `1080p`, `720p`, `480p`, `240p`
  - **Help**: Defines the quality of the videos.

- `--video_modifications`
  - **Default**: `no_modification`
  - **Choices**: `no_modification`, `blur`, `noise`, `black_and_white`, `distortion`, `different_color_space`
  - **Help**: Specifies the modifications for the video.

### frame_videos.py

Example command:
```bash
python3 utils/frame_videos.py --time 00:23 00:55 01:01 01:23 02:34 02:55 03:15 03:44 04:02 04:45 --video_quality 480p --video_modifications no_modification
```

#### Arguments

- `--video_input`
  - **Help**: Path to the video file.
  - **Explanation**: Specifies the path to the video. This argument is required for the script to run.

- `--frames_output`
  - **Default**: `../data/frames`
  - **Help**: Path to the folder containing the frames of a video.
  - **Explanation**: Specifies the output folder for video frames. This argument is optional.

- `--time`
  - **Help**: List of times in the format `MM:SS`.
  - **Explanation**: Specifies the timestamps for extracting frames. This argument is required.

- `--video_quality`
  - **Default**: `1080p`
  - **Choices**: `1080p`, `720p`, `480p`, `240p`
  - **Help**: Defines the quality of the videos.

- `--video_modifications`
  - **Default**: `no_modification`
  - **Choices**: `no_modification`, `blur`, `noise`, `black_and_white`, `distortion`, `different_color_space`
  - **Help**: Specifies the modifications for the video.
