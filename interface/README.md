# Interface

## Dependencies

To get started, install the necessary dependencies:

```bash
pip install Flask
pip install markdown
```

Ensure you have `torch` and `torchvision` installed. You can find the installation files on the [NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048).

For JetPack 6.0 (L4T R36.2 / R36.3) + CUDA 12.4, use the following links:

- [torch 2.3](https://nvidia.box.com/shared/static/zvultzsmd4iuheykxy17s4l2n91ylpl8.whl)
- [torchvision 0.18](https://nvidia.box.com/shared/static/u0ziu01c0kyji4zz3gxam79181nebylf.whl)

## Running the Application

To start the Flask application, run the following command:

```bash
python ./interface/src/app.py
```

Then, open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

### Video transcription mode

1. Select a video file within the interface in your web browser.
2. Select a frame rate to analyze images (up to 120 frames per minute). Note, a warning may appear if you request to analyze more frames than are available in the total video.
3. Click "Start Transcription" and wait for the frame description to complete.

Enjoy using the interface for your video analysis tasks!

Additionally, a log file is generated in `interface/data/logs/` containing the frame numbers, timestamps and transcriptions.

### Question & Answering mode

1. Load the log file generated from the video transcription mode.
2. Enter your question.
3. Wait for the model to provide an answer.

We use the Qwen model with 500 million parameters. The maximum context length is approximately 32,000 tokens. Each query to the Qwen model includes the transcription, the question, and a pre-prompt. Ensure the combined input is within the 32,000 token limit to provide complete information to the model.

Note that each query is independent, and previous questions and answers are not included in subsequent queries.

In `Qwen25.py`, there is a parameter `max_new_tokens=100`. We have capped it to 100 to get answers quickly (as fewer tokens need to be generated), but you can change it.