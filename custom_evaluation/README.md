# Custom Evaluation Function

## Overview

This repository contains the `custom_evaluation` function, which is designed to evaluate VLM performance with respect to different video qualities and degradations.

## Installation

To install the necessary dependencies, first ensure `pip` is up to date:
```bash
python -m pip install --upgrade pip
```
Then run:
```bash
pip install --upgrade pip setuptools wheel
```
This will avoid the error: `ERROR: Could not build wheels for opencv-python which use PEP 517 and cannot be installed directly`.

Next, run:
```bash
pip install -r requirements.txt
```
Then, ensure all the necessary NLTK data files are downloaded by running:
```bash
python custom_evaluation/utils/compute_similarity/nltk_download.py 
```

## Usage

### Step 1: Generate Degraded Videos and Frames

First, navigate to the folder `code`:
```bash
cd custom_evaluation/code
```

Generate degraded videos and frames from an input video by running the `degrade_frame_videos.py` script. Use the following command as an example:
```bash
python3 degrade_frame_videos.py --video_path ../data/cam-philippines-5min.mp4 --output_fps 1 --time 00:23 00:55 01:01 01:23 02:34 02:55 03:15 03:44 04:02 04:45 --video_quality 480p --video_modifications no_modification
```

#### `degrade_frame_videos` arguments

- `--video_path`
  - **Help**: Path to the video file.
  - **Explanation**: Specifies the path to the video. This argument is required for the script to run.

- `--videos_output`
  - **Default**: `../data/videos_degraded`
  - **Help**: Path to the folder containing the degraded videos.
  - **Explanation**: Specifies the output folder for degraded videos. This argument is optional.

- `--frames_output`
  - **Default**: `../data/frames`
  - **Help**: Path to the folder containing the frames of a video.
  - **Explanation**: Specifies the output folder for video frames. This argument is optional.

- `--output_fps`
  - **Default**: `0`
  - **Help**: Output FPS for the degraded videos. Defaults to the same FPS as the input video.

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

The arguments `video_quality` and `video_modifications` are combined to create the videos and frames. For example, if you choose `1080p` and `720p` for quality, and `blur` and `noise` for modifications, the script will generate videos and frames for `1080p_blur`, `1080p_noise`, `720p_blur`, and `720p_noise`.

To degrade videos and extract frames separately, use the scripts `degrade_videos.py` and `frame_videos.py` located in the `utils` folder.

### Step 2: Generate Model Outputs

Using the frames created in the first step, feed the model to get results by running the `questionModel.py` script. Example command:
```bash
python3 questionModel.py --model MiniCPMV2 --video_quality 1080p 720p --video_modifications no_modification black_and_white
```

#### `questionModel` arguments

- `--model`
  - **Default**: `Moondream2`
  - **Help**: Specifies the model to be used.

- `--question`
  - **Default**: `Describe this image.`
  - **Help**: Specifies the question to send to the model.

- `--input_frames`
  - **Default**: `../data/frames`
  - **Help**: Path to the folder containing the frames of a video.

- `--result_output`
  - **Default**: `../data/results_model`
  - **Help**: Path to the folder where the results will be stored.

- `--video_quality`
  - **Default**: `1080p`
  - **Choices**: `1080p`, `720p`, `480p`, `240p`
  - **Help**: Defines the quality of the videos.

- `--video_modifications`
  - **Default**: `no_modification`
  - **Choices**: `no_modification`, `blur`, `noise`, `black_and_white`, `distortion`, `different_color_space`
  - **Help**: Specifies the modifications for the video.

This script generates JSON files containing the description of each frame for each type of video.

### Step 3: Evaluate Results

Evaluate the results against a ground truth text file. There are two methods for comparing model transcriptions with the ground truth:

1. **Keyword Comparison**: Computes the Jaccard similarity based on keywords.
2. **Sentence Transformer**: Computes text embeddings using a Sentence Transformer model.

#### Example Command (Using Sentence Transformer):
```bash
python3 evaluateModels.py --evaluation_mode ST --write_results
```

#### `evaluateModels` arguments

- `--ground_truth_path`
  - **Default**: `../data/ground_truth/ground_truth.json`
  - **Help**: Path to the ground truth file.
  - **Explanation**: Specifies the path to the ground truth text file containing correct transcriptions. This argument is required.

- `--candidates_path_folder`
  - **Default**: `../data/results_model`
  - **Help**: Path to the folder containing candidate files.
  - **Explanation**: Specifies the folder containing candidate transcription files to be evaluated. This argument is required.

- `--ST_model_name`
  - **Default**: `all-MiniLM-L6-v2`
  - **Help**: Name of the model for computing similarity with Sentence Transformer.
  - **Explanation**: Specifies the Sentence Transformer model to use for text similarity computation. This argument is optional.

- `--write_results`
  - **Help**: Flag to write the results to a file.
  - **Explanation**: When set, this flag indicates that results should be written to a file. It does not take a value and is used as a boolean flag.

- `--output`
  - **Default**: `../data/benchmark_score`
  - **Help**: Path to the output file for evaluation results.
  - **Explanation**: Specifies the output file for writing evaluation results.

- `--evaluation_mode`
  - **Choices**: `ST`, `JKW`
  - **Required**: `True`
  - **Help**: Specifies the evaluation mode: `ST` for Sentence Transformer or `JKW` for Jaccard Keyword.

- `--text_file`
  - **Help**: Flag to indicate that the input files are text files. Defaults to JSON.

This script generates scores for each JSON file containing model-generated descriptions.
