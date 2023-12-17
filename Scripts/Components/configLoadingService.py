import json


def load_color_scheme(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config["color_scheme"]
    except FileNotFoundError:
        print(f"Color configuration file not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print("Error parsing JSON configuration file.")
        return None
    except Exception as e:
        print(f"Error loading color scheme: {e}")
        return None
