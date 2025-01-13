import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

def create_cellular_network(cluster_size=7, grid_size=4):
    # Colors for different frequency groups
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']
    
    # Hexagon size
    hex_size = 1.0
    
    # Cluster pattern parameters
    i, j = 2, 1  # Define the cluster pattern
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Calculate positions for hexagonal cells
    for row in range(-grid_size, grid_size + 1):
        for col in range(-grid_size, grid_size + 1):
            # Calculate center position of each hexagon
            x = col * 3 * hex_size / 2
            y = (row * np.sqrt(3) * hex_size) + (col % 2) * (np.sqrt(3) * hex_size / 2)
            
            # Frequency group calculation
            freq_group = (i * row + j * col) % cluster_size
            
            # Ensure positive frequency group (modulo can give negative values)
            freq_group = freq_group if freq_group >= 0 else freq_group + cluster_size
            
            # Create hexagonal cell
            hexagon = RegularPolygon((x, y), numVertices=6, radius=hex_size,
                                     orientation=np.pi / 6,
                                     facecolor=colors[freq_group],
                                     alpha=0.4,
                                     edgecolor='black')
            ax.add_patch(hexagon)
            
            # Add frequency group number
            plt.text(x, y, str(freq_group + 1), ha='center', va='center')

    # Set equal aspect ratio and limits
    ax.set_aspect('equal')
    plt.xlim(-grid_size * 2, grid_size * 2)
    plt.ylim(-grid_size * 2, grid_size * 2)
    
    # Add title and labels
    plt.title(f'Cellular Network with {cluster_size}-Cell Cluster Pattern')
    plt.xlabel('Distance')
    plt.ylabel('Distance')

# Create and display the network
create_cellular_network()

plt.grid(False)
plt.show()
