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

1. Place a video file in the `interface/data/videos/` folder.
2. Select the video file within the interface in your web browser.
3. Select a frame rate to analyze images.
4. Click "Start Transcription" and wait for the frame description to complete.

Enjoy using the interface for your video analysis tasks!