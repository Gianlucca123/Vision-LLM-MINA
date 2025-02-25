# Installation and Launch of VILA

This guide explains how to install and run **VILA** on the **Jetson Orin Nano** board.

We followed the NVIDIA lab tutorial to perform this installation: [https://www.jetson-ai-lab.com/tutorial_nano-vlm.html](#)

## 1. Installing NanoLLM and VILA

Run the following command to install and execute **NanoLLM** and **VILA**:

```bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.chat --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 64 \
    --max-new-tokens 32
```
After installation, the VILA model will be automatically launched, and you can start querying it.

## 2. Querying VILA on an Image

**Note:** Images must be placed in the `jetson-containers/data/images/` directory.

To ask questions, type in the interface that opens after launching:
```bash
>> PROMPT: /data/images/my_image.png

>> PROMPT: I ask my question here.
```

Feel free to reset the questioning process to provide another image or prevent the model from relying on previous answers using **reset**:
```bash
>> PROMPT: reset
```

### Preparing Prompts in Advance

You can structure your questions in advance as follows:

```bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.chat --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 256 \
    --max-new-tokens 32 \
    --prompt '/data/images/hoover.jpg' \
    --prompt 'what does the road sign say?' \
    --prompt 'what kind of environment is it?' \
    --prompt 'reset' \
    --prompt '/data/images/lake.jpg' \
    --prompt 'please describe the scene.' \
    --prompt 'are there any hazards to be aware of?'
```

📌 **Note:**
- The first prompt must contain the path of the image to analyze.
- The `reset` keyword resets the discussion history and allows for submitting a new image.

## 3. Querying VILA in Direct Mode

```bash
jetson-containers run $(autotag nano_llm) \
  python3 -m nano_llm.agents.video_query --api=mlc \
    --model Efficient-Large-Model/VILA1.5-3b \
    --max-context-len 256 \
    --max-new-tokens 32 \
    --video-input /dev/video0 \
    --video-output webrtc://@:8554/output
```

---

This guide provides a clear procedure for using **VILA** on the **Jetson Orin Nano**. For more details, refer to the official NVIDIA documentation.
