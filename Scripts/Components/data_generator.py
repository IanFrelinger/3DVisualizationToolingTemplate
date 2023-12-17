import numpy as np


def generate_data(num_points=100):
    try:
        # Generate random x, y, z coordinates
        x = np.random.normal(size=num_points)
        y = np.random.normal(size=num_points)
        z = np.random.normal(size=num_points)

        # Calculate intensity
        intensity = np.sqrt(x ** 2 + y ** 2 + z ** 2)

        return {
            "x": x,
            "y": y,
            "z": z,
            "intensity": intensity
        }
    except Exception as e:
        print(f"Error generating data: {e}")
        return None
