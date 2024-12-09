# Custom Evaluation Function

## Overview

This repository contains the `custom_evaluation` function, which is designed to evaluate VLM performance regarding to different video quality/degradation.

## Installation

To install the necessary dependencies, first ensure having pip up to date:
```bash
python -m pip install --upgrade pip
```
Then run:
```bash
pip install --upgrade pip setuptools wheel
```
This will avoid the error: 'ERROR: Could not build wheels for opencv-python which use PEP 517 and cannot be installed directly'.

Then, run :
```bash
pip install -r .\requirements.txt
```
Then, run nltk_download to ensure having all the necessary NLTK data files.

```bash
python .\custom_evaluation\utils\compute_similarity\nltk_download.py 
``` 


## Usage
First, generate degraded videos from an input video by running the `genVideo.py` script. Use the following command as an example:

    python .\genVideo.py --video_path "data/input/cam-philippines-5min.mp4" --output_folder_path "data/output/" --output_fps 1

Where `video_path` is the input path to the video file you want to process. This should be a string representing the file path. `output_folder_path`
is the directory where the generated degraded videos will be saved. `output_fps` is the frames per second rate for the output video.

Second, export transcription => TODO

Third, evaluate results regarding a ground truth text file.
There are two ways of comparing models transcriptions with the ground truth:
- by comparing the key words and computing with the Jaccard similarity.
- by using a sentence transformer and computing text embeddings.

To evaluate using the Jaccard keywords similarity run:

    python .\evaluateBestTranscription.py --ground_truth_path "data/input/ground_truth/flying_whales.txt" --candidates_path_folder "data/output/transcription" --write_results --output_path "data/output/benchmark/output_JKW.txt" --evaluation_mode "JKW" --text_file

To evaluate using the sentence transformer, run:

    python .\evaluateBestTranscription.py --ground_truth_path "data/input/ground_truth/flying_whales.txt" --candidates_path_folder "data/output/transcription" --write_results --output_path "data/output/benchmark/output_ST.txt" --evaluation_mode "ST" --text_file


### evaluateBestTranscription arguments

- `--ground_truth_path`
    - **default**: "data/input/ground_truth/ground_truth.txt"
    - **help**: Path to the ground truth file.
    - **Explanation**: This argument specifies the path to the ground truth text file that contains the correct transcriptions. It is required for the script to run.

- `--candidates_path_folder`
    - **default**: "data/output/transcriptions/"
    - **help**: Path to the folder containing candidate files.
    - **Explanation**: This argument specifies the path to the folder containing the candidate transcription files that need to be evaluated. It is required for the script to run.

- `--ST_model_name`
    - **default**: "all-MiniLM-L6-v2"
    - **help**: Name of the model to use for computing similarity with Sentence Transformer.
    - **Explanation**: This argument specifies the name of the Sentence Transformer model to use for computing text similarity. It is optional and defaults to "all-MiniLM-L6-v2".

- `--write_results`
    - **help**: Flag to write the results to a file.
    - **Explanation**: This argument is a flag that, when set, indicates that the results should be written to a file. It does not take any value and is used as a boolean flag.

- `--output_path`
    - **default**: "data/output/benchmark/output.txt"
    - **help**: Path to the output file where results will be written.
    - **Explanation**: This argument specifies the path to the output file where the evaluation results will be written. It is optional and defaults to "data/output/benchmark/output.txt".

- `--evaluation_mode`
    - **type**: str
    - **choices**: ["ST", "JKW"]
    - **required**: True
    - **help**: Evaluation mode to use: 'ST' for Sentence Transformer or 'JKW' for Jaccard Keyword.
    - **Explanation**: This argument specifies the evaluation mode to use. It can be either "ST" for Sentence Transformer or "JKW" for Jaccard Keyword. It is required for the script to run.

- `--text_file`
    - **action**: "store_true"
    - **help**: Flag to indicate that the input files are text files. Default is JSON.
    - **Explanation**: This argument is a flag that, when set, indicates that the input files are text files instead of JSON files. It does not take any value and is used as a boolean flag.