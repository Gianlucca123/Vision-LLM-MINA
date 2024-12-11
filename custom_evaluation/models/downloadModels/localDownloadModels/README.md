# VLM Local Download

## Instructions

1. **Download the huggingface folder**  
   First, you need to download the `/huggingface` folder to your desired path. This action will download ALL the models at once, so make sure you have sufficient disk space available.

2. **Locate the .cache directory**  
   Next, you need to locate the `.cache` directory. You can do this by running the following command in your terminal:
   ```bash
   find ~ -type d -name ".cache"
   ```
   The correct path should look like `home/user/.cache`

3. **Copy the huggingface folder**  
   Finally, you will need to execute a script to copy the `/huggingface` folder to the `.cache` directory. Use the following command:
    ```bash
    python copy_huggingface_cache.py source_dir destination_dir
    ```
   Replace `source_dir` and `destination_dir` with your actual source and destination directories. For example : `home/user/Desktop/huggingface` and `home/user/.cache`.


## Notes
This copy can be done both ways.

Have fun!