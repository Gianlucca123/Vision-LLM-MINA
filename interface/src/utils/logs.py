import os
from datetime import datetime

def define_log_file():
    """
    @brief Creates a log file path with a timestamped filename.
    This function checks if the log directory exists, and if not, it creates it.
    It then generates a log file name with the current timestamp and returns the full path to the log file.
    @return str The full path to the log file.
    """

    log_path = "interface/data/logs"
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # define a file name for the log file containing the timestamp
    log_file_name = (
        f"transcription_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    )

    log_file_path = os.path.join(log_path, log_file_name)

    return log_file_path


def write_logs(answer, timestamp, frame_id, log_file_path):
    """
    @brief Writes logs to a specified file.
    This function appends the provided answer, timestamp, and frame ID to the specified log file.
    Each log entry is separated by a line of dashes.
    @param answer The answer to be logged.
    @param timestamp The timestamp associated with the log entry.
    @param frame_id The frame ID associated with the log entry.
    @param log_file_path The path to the log file where the entry should be written.
    @return None
    """

    # write the answer to the logs with the timestamp and frame ID
    with open(log_file_path, "a") as log_file:
        log_file.write(f"Frame ID: {frame_id}\n")
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write(f"Answer: {answer}\n")
        log_file.write("-" * 50 + "\n")
        log_file.flush()
