# VLM Local Download

## Instructions

1. **Download the huggingface folder**  
   First, you need to download the `/huggingface` folder to your desired path. This action will download ALL the models at once, so make sure you have sufficient disk space available.

2. **Locate the .cache directory**  
   Next, you need to locate the `.cache` directory. 
   
   You can do this by running the following command in your terminal:
   ```bash
   find ~ -type d -name ".cache"
   ```
   The correct path should look like `home/user/.cache`

3. **Insert the huggingface folder**  
   Finally, you will need to insert the `/huggingface` folder in the `.cache` directory.

   To achieve this, you can use the `mv` command:
   ```bash
   mv huggingface .cache/
   ```
   Ajust the according repositories. For example: `home/user/Desktop/huggingface` and `home/user/.cache`.

## Notes
MiniCPMV2 cannot run offline. For more information check `onlineDownloadModels/README.md`.