# Custom Evaluation Function

## Overview

This repository contains the `custom_evaluation` function, which is designed to evaluate VLM performance regarding to different video quality/degradation.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage
First, generate degraded videos from an input video by running the `genVideo.py` script. Use the following command as an example:

    python .\genVideo.py --video_path "data/input/cam-philippines-5min.mp4" --output_folder_path "data/output/" --output_fps 1

Where `video_path` is the input path to the video file you want to process. This should be a string representing the file path. `output_folder_path`
is the directory where the generated degraded videos will be saved. `output_fps` is the frames per second rate for the output video.

