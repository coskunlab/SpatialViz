This forlder contains the scripts and data to reproduce the result in the paper "Spatially visualized single-cell pathology of highly multiplexed protein profiles in health and disease"

# Organization

## Data
"data" folder contains all the necessary data to reproduce the results in the paper:
- "raw" folder contains all the gray scale image of IMC for each Region of Interest (ROI) for each marker
- "masks" folder contains all the binary mask from IMC imgaes defined by thresholding 
- "cell_masks" folder contains all the single cell segmentation for each ROI
- "clusters" folder contains the anatomical clustering of each ROI 

## Notebooks 
"notebooks" folder contains jupyter notebook script used:
    - 01_image_level_clustering is the script for performing KMeans clustering of marker images
    - 02_cluster_representation is the script for generating combined image of mean cluster images
    - 03_marker_stats is the script for generating statistical plot of combination of ROI such as area and expression level 
    - 04_spatial_proximity_plot is the script for plotting spatial proximity for pair of markers from a ROI
    - 05_topographic_map is the script for generating 3D visualization of markers from a ROI
    - 06_stats_plot is the script for generating statistical plot for individual ROI 

## Source code
"src" folder contains customs python scripts module used

## Figures 
"figures" folder contains generated figures for the paper

