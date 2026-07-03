import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
# Force Matplotlib to work without GUI
matplotlib.use("Agg") 

# 1. Load Iris Data
def load_iris_data(filepath):
    """
    Load the Iris dataset from CSV.
    """
    try:
        df = pd.read_csv(filepath)
        
        print("Iris dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


# 2. Feature Distribution (Histograms)
def plot_feature_distributions(df):
    """
    Create and save a 2x2 grid of histograms to show data distribution.
    Visualizing feature distributions using histograms.
    """
    # Create a figure with 2 rows and 2 columns
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Iris Feature Distributions")

    # Plotting histograms for each feature
    df['SepalLengthCm'].hist(ax=axes[0, 0], color='skyblue', bins=15, edgecolor='black')
    axes[0, 0].set_title('Sepal Length (Cm)')

    df['SepalWidthCm'].hist(ax=axes[0, 1], color='salmon', bins=15, edgecolor='black')
    axes[0, 1].set_title('Sepal Width (Cm)')

    df['PetalLengthCm'].hist(ax=axes[1, 0], color='lightgreen', bins=15, edgecolor='black')
    axes[1, 0].set_title('Petal Length (Cm)')

    df['PetalWidthCm'].hist(ax=axes[1, 1], color='gold', bins=15, edgecolor='black')
    axes[1, 1].set_title('Petal Width (Cm)')

    plt.tight_layout()
    
    # Save the plot
    output_file = "iris_distributions.png"
    plt.savefig(output_file)
    print(f"Distributions plot saved to {output_file}")


# 3. 3D Scatter + Line Plot
def plot_3d_clusters(df):
    """
    Visualize species in 3D space and connect their averages with a line.
    """
    fig = plt.figure(figsize=(10, 8))

    # Create 3D axes
    ax = fig.add_subplot(111, projection='3d')
    
    # Colors for the species
    colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
    
    # Part A: 3D Scatter Plot
    for species, group in df.groupby('Species'):
        ax.scatter(
            group['SepalLengthCm'],  # X Axis
            group['SepalWidthCm'],   # Y Axis
            group['PetalLengthCm'],  # Z Axis

            # Apply the color based on species
            c=colors.get(species, 'black'),
            label=species,
            s=50,
            alpha=0.6
        )

    # Part B: 3D Line Plot (Evolutionary Path)
    # Calculate the average (mean) position of each species

    # We drop 'Id' and 'Species' (non-numeric) before calculating mean
    numeric_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    means = df.groupby('Species')[numeric_cols].mean()
    
    # Draw a line connecting the centers of the clusters
    ax.plot(
        means['SepalLengthCm'], 
        means['SepalWidthCm'], 
        means['PetalLengthCm'], 
        color='black', 
        linewidth=3, 
        linestyle='--', 
        label='Cluster Center Path'
    )
    
    # Add labels
    ax.set_title("3D Species Clusters & Trends")
    ax.set_xlabel("Sepal Length (Cm)")
    ax.set_ylabel("Sepal Width (Cm)")
    ax.set_zlabel("Petal Length (Cm)")
    ax.legend()
    
    # Save the plot
    output_file = "iris_3d_scatter.png"
    plt.savefig(output_file)
    print(f"3D Scatter plot saved to {output_file}")


# 4. Plot Filled Contour Map
def plot_contour_map(df):
    """
    Create a filled contour map to represent elevation using Petal Width.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = df['SepalLengthCm']
    y = df['SepalWidthCm']

    # Using Petal Width as the "elevation"
    z = df['PetalWidthCm']

    # tricontourf creates a filled contour from scattered data points
    contour = ax.tricontourf(x, y, z, levels=14, cmap='inferno')
    
    # Add a color bar
    cbar = plt.colorbar(contour)
    cbar.set_label('Petal Width (Elevation)')

    # [IMPROVEMENT]: Overlay the original points so we can see the data density
    ax.scatter(x, y, c='black', s=10, alpha=0.3, label='Data Points')
    
    ax.set_title("Topological Map of Petal Width")
    ax.set_xlabel("Sepal Length (Cm)")
    ax.set_ylabel("Sepal Width (Cm)")
    ax.legend()
    
    # Save the plot
    output_file = "iris_contour_map.png"
    plt.savefig(output_file)
    print(f"Contour map saved to {output_file}")


if __name__ == "__main__":
    
    # Load Data
    df = load_iris_data("iris.csv")
    
    if not df.empty:
        # 1. Visualization: Histograms
        print("\nGenerating Histograms...")
        plot_feature_distributions(df)
        
        # 2. Visualization: 3D Scatter
        print("\nGenerating 3D Scatter Plot...")
        plot_3d_clusters(df)
        
        # 3. Visualization: Contour Map
        print("\nGenerating Contour Map...")
        plot_contour_map(df)


