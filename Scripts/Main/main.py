from Scripts.Components.data_generator import generate_data
from Scripts.Components.graphing_service import plot_data
from Scripts.Components.config_commons import JSON_CONFIG_PATH
from Scripts.Components.configLoadingService import load_color_scheme


def main():
    try:
        # Use the common JSON config path
        color_scheme = load_color_scheme(JSON_CONFIG_PATH)
        if color_scheme is None:
            raise ValueError("Failed to load color scheme.")

        print(color_scheme)
        data = generate_data(100)
        plot_data(data, color_scheme)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
