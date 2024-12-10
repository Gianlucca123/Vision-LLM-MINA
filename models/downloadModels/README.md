# VLM Model Downloader

This repository provides scripts to download and set up various VLM models. Each model has a corresponding script that must be executed to download and prepare the model for use.

## Instructions

1. **Install Requirements**  
   Before proceeding, ensure that all required dependencies are installed. You can do this by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Models**  
   Each model has its own download script in the repository. You need to execute these scripts individually to download the respective models. For example:
    ```bash
    python3 download_Modelname.py
    ```
    Replace `Modelname` with the name of the model you wish to download. Repeat this step for each model you need.

3. **Additional Fix for MiniCPM**  
   If you plan to use the MiniCPM model, please note that there is an additional fix required for it to function correctly. You can find the necessary files and instructions in the `MiniCPMFix` folder. Be sure to follow the instructions provided in that folder after running the `download_MiniCPM.py` script.

## Notes
Make sure you have sufficient disk space and a stable internet connection for downloading the models.
If you encounter any issues, check the respective model's documentation or reach out for support.

Have fun!