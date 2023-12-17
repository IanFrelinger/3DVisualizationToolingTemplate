import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def plot_data(data, color_scheme):
    try:
        # Example custom color scheme
        colors = [(0, 0, 1), (1, 0, 0)]  # Blue to red
        positions = [0, 1]  # Start and end
        custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", list(zip(positions, colors)))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        scatter = ax.scatter(data["x"], data["y"], data["z"], c=data["intensity"], cmap=custom_cmap)
        fig.colorbar(scatter, ax=ax, label='Intensity')
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.set_title('3D Spherical Volumetric Data Plot')
        plt.show()
    except Exception as e:
        print(f"Error while plotting data: {e}")
