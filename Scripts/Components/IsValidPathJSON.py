import os
import json


def is_valid_json(file_path):
    """
    Validates if the provided file path points to a valid JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    bool: True if the file is a valid JSON, False otherwise.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False

    try:
        with open(file_path, 'r') as file:
            # Attempt to parse the JSON
            json.load(file)
        return True
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
