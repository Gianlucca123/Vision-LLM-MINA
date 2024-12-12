# VLM Online Download

This repository provides scripts to download and set up various VLM models. Each model has a corresponding script that must be executed to download and prepare the model for use.

## Instructions

1. **Download Models**  
   Each model has its own download script in the repository. You need to execute these scripts individually to download the respective models. For example:
    ```bash
    python3 download_Modelname.py
    ```
   Replace `Modelname` with the name of the model you wish to download. Repeat this step for each model you need.

3. **Additional Step and Fix for MiniCPM**  
   If you plan to use the MiniCPM model, please note that there is an additional step and the additional fix required for it to function correctly. 

   The additionnal STEP requires you to create a `.env` file in the `Vision-LLM-MINA/` directory with a line to create a hugging face key variable under this format :
    ```bash
    HUGGINGFACE_HUB_TOKEN="your_hugging_key"
    ```
   
   You can find the necessary FIX files and instructions in the `MiniCPMFix` folder. Be sure to follow the instructions provided in that folder after running the `download_MiniCPM.py` script.

## Notes
Make sure you have sufficient disk space and a stable internet connection for downloading the models.
If you encounter any issues, check the respective model's documentation or reach out for support.

Have fun!