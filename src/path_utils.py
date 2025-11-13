import os

from dotenv import load_dotenv

load_dotenv()


def get_data_dir() -> str:
    """Get the full path to a data file located in the 'data' directory.

    Args:
        filename (str): The name of the data file.
    Returns:
        str: The full path to the data file.
    """
    try:
        base_dir = os.environ["SOURCE_DATA_DIR"]
    except KeyError:
        raise KeyError("Environment variable 'DATA_DIR' not set.")
    return base_dir


def get_logs_dir() -> str:
    """Get the logs directory path.

    Returns:
        str: The logs directory path.
    """
    try:
        logs_dir = os.environ["LOGS_DIR"]
    except KeyError:
        raise KeyError("Environment variable 'LOGS_DIR' not set.")
    return logs_dir


def get_configs_dir() -> str:
    """Get the configs directory path.

    Returns:
        str: The configs directory path.
    """
    try:
        configs_dir = os.environ["CONFIGS_DIR"]
    except KeyError:
        raise KeyError("Environment variable 'CONFIGS_DIR' not set.")
    return configs_dir
