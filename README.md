# Iris-3D-Mapper-Project

Visualizing Biological Data in 3D Space

Hey Innovators! Welcome to Project 2: Iris 3D Mapper Project! 🌸🌿

Biologists often analyze plant measurements to understand how different species vary and cluster in nature. One of the most famous datasets used for this purpose is the Iris Flower Dataset.
Chef wants to visually explore this biological data to answer big questions:

Can we visually identify clusters of species in 3D space?
How do petal and sepal dimensions interact?
What does the "terrain" of petal width look like?
Your task is to transform raw biological data into meaningful visual insights using Subplots, 3D Scatter Plots, and Filled Contour Maps.

Important Notes
You are given a single file: main.py:

Do NOT change function names: The testing system relies on them.
Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
All functions are already defined in main.py. You need to complete the missing logic.
Dataset
You will work with a CSV file named iris.csv.

Columns Description:
SepalLengthCm → Length of the sepal (cm)
SepalWidthCm → Width of the sepal (cm)
PetalLengthCm → Length of the petal (cm)
PetalWidthCm → Width of the petal (cm)
Species → "Iris-setosa", "Iris-versicolor", "Iris-virginica"
Dataset Preview (First 5 rows):
Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
1,5.1,3.5,1.4,0.2,Iris-setosa
2,4.9,3.0,1.4,0.2,Iris-setosa
3,4.7,3.2,1.3,0.2,Iris-setosa
4,4.6,3.1,1.5,0.2,Iris-setosa
5,5.0,3.6,1.4,0.2,Iris-setosa
Your Tasks
Load Iris Data
Inside load_iris_data(filepath):
Read the CSV file using Pandas.
Return the DataFrame (code provided).
Docs: pandas.read_csv()
Feature Distribution (Histograms)
Inside plot_feature_distributions(df):
Goal: Compare the spread of all 4 features at a glance.
Layout: Create a 2 × 2 grid of subplots.
Figure Size: Set the figure size to 10 inches by 8 inches (code provided).
Plotting Requirements: Create a histogram for each feature in the specific subplot:
(0,0) Histogram of SepalLengthCm (Color: skyblue)
(0,1) Histogram of SepalWidthCm (Color: salmon)
(1,0) Histogram of PetalLengthCm (Color: lightgreen)
(1,1) Histogram of PetalWidthCm (Color: gold)
Common Settings:
Number of bins = 15 (Explore the bins parameter).
Color of edge = black (Explore the edgecolor parameter).
Save: Save as iris_distributions.png (code provided)
Adjust the spacing using plt.tight_layout().
Docs: matplotlib.pyplot.subplots | pandas.Series.hist | matplotlib.pyplot.tight_layout | matplotlib.pyplot.savefig
3D Species Clustering
Inside plot_3d_clusters(df):
Goal: Visualize how the three species cluster in a 3D volume.
Part A: 3D Scatter Plot
Initialize a 3D projection subplot.
Loop through the data grouped by species.
Inside the loop, create a scatter plot for the current group:
X-axis: SepalLengthCm
Y-axis: SepalWidthCm
Z-axis: PetalLengthCm
Color Mapping: (code provided)
Use the provided colors dictionary to find the color for the current species. Use "black" as the default/fallback color if the species is not found (Explore the c parameter and dictionary .get() method).
Styling:
Size = 50 (Explore the s parameter).
Transparency = 0.6 (Explore the alpha parameter).
Set label as species, this is important for legend (Explore the label parameter).
Part B: Evolutionary Path (Centroids)
Calculate the Mean (Average) of the columns grouped by Species.
The Line: Draw a dashed black line connecting the centroids of the 3 species.
Use the Mean X, Y, and Z values calculated above.
Color should be black, Width of line: 3, Line should be dashed (Explore the color, linewidth and linestyle parameters).
Label: "Cluster Center Path".
Save: Save as iris_3d_scatter.png (code provided).
Docs: Matplotlib 3D Scatter Plots | Matplotlib 3D Line Plots | pandas.DataFrame.groupby | Matplotlib Linestyles
Filled Contour Map
Inside plot_contour_map(df):
Goal: Create a topological map where "Petal Width" represents the elevation.
Axes:
X: SepalLengthCm
Y: SepalWidthCm
Z (Elevation): PetalWidthCm
The Map:
Use ax.tricontourf() to create a filled contour.
Number of levels: 14
Colormap: 'inferno'
Add a Colorbar labeled "Petal Width (Elevation)" (Explore the label parameter).
The Overlay:
Plot the original data points on top so we can see where the data actually exists.
Color of points should be black, Size of points: 10, Transparency: 0.3 (Explore the color, s and alpha parameters).
Label: "Data Points"
Save: Save as iris_contour_map.png (code provided).
Docs: matplotlib.pyplot.tricontourf | Matplotlib Colormaps | matplotlib.pyplot.colorbar | matplotlib.pyplot.scatter
Expected Output:
When you run the code, your program should print the following messages and generate three image files in the same directory:

Console Output:
Iris dataset loaded successfully.

Generating Histograms...
Distributions plot saved to iris_distributions.png

Generating 3D Scatter Plot...
3D Scatter plot saved to iris_3d_scatter.png

Generating Contour Map...
Contour map saved to iris_contour_map.png
Generated Files:
iris_distributions.pngimage
iris_3d_scatter.pngimage
iris_contour_map.pngimage
