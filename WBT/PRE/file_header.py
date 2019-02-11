import arcpy
from WBT.whitebox_tools import WhiteboxTools
wbt = WhiteboxTools()
wbt.set_verbose_mode(True)

tool_labels = []
tool_labels.append("Absolute Value")
tool_labels.append("Adaptive Filter")
tool_labels.append("Add")
tool_labels.append("Add Point Coordinates To Table")
tool_labels.append("Aggregate Raster")
tool_labels.append("And")
tool_labels.append("Anova")
tool_labels.append("Arc Cos")
tool_labels.append("Arc Sin")
tool_labels.append("Arc Tan")
tool_labels.append("Aspect")
tool_labels.append("Atan2")
tool_labels.append("Attribute Correlation")
tool_labels.append("Attribute Histogram")
tool_labels.append("Attribute Scattergram")
tool_labels.append("Average Flowpath Slope")
tool_labels.append("Average Overlay")
tool_labels.append("Average Upslope Flowpath Length")
tool_labels.append("Balance Contrast Enhancement")
tool_labels.append("Basins")
tool_labels.append("Bilateral Filter")
tool_labels.append("Block Maximum Gridding")
tool_labels.append("Block Minimum Gridding")
tool_labels.append("Breach Depressions")
tool_labels.append("Breach Single Cell Pits")
tool_labels.append("Buffer Raster")
tool_labels.append("Ceil")
tool_labels.append("Centroid")
tool_labels.append("Centroid Vector")
tool_labels.append("Change Vector Analysis")
tool_labels.append("Circular Variance Of Aspect")
tool_labels.append("Classify Overlap Points")
tool_labels.append("Clip")
tool_labels.append("Clip Lidar To Polygon")
tool_labels.append("Clip Raster To Polygon")
tool_labels.append("Closing")
tool_labels.append("Clump")
tool_labels.append("Compactness Ratio")
tool_labels.append("Conservative Smoothing Filter")
tool_labels.append("Construct Vector Tin")
tool_labels.append("Convert Nodata To Zero")
tool_labels.append("Convert Raster Format")
tool_labels.append("Corner Detection")
tool_labels.append("Correct Vignetting")
tool_labels.append("Cos")
tool_labels.append("Cosh")
tool_labels.append("Cost Allocation")
tool_labels.append("Cost Distance")
tool_labels.append("Cost Pathway")
tool_labels.append("Count If")
tool_labels.append("Create Colour Composite")
tool_labels.append("Create Hexagonal Vector Grid")
tool_labels.append("Create Plane")
tool_labels.append("Create Rectangular Vector Grid")
tool_labels.append("Crispness Index")
tool_labels.append("Cross Tabulation")
tool_labels.append("Cumulative Distribution")
tool_labels.append("D Inf Flow Accumulation")
tool_labels.append("D Inf Mass Flux")
tool_labels.append("D Inf Pointer")
tool_labels.append("D8 Flow Accumulation")
tool_labels.append("D8 Mass Flux")
tool_labels.append("D8 Pointer")
tool_labels.append("Decrement")
tool_labels.append("Depth In Sink")
tool_labels.append("Dev From Mean Elev")
tool_labels.append("Diff From Mean Elev")
tool_labels.append("Diff Of Gaussian Filter")
tool_labels.append("Difference")
tool_labels.append("Direct Decorrelation Stretch")
tool_labels.append("Directional Relief")
tool_labels.append("Dissolve")
tool_labels.append("Distance To Outlet")
tool_labels.append("Diversity Filter")
tool_labels.append("Divide")
tool_labels.append("Downslope Distance To Stream")
tool_labels.append("Downslope Flowpath Length")
tool_labels.append("Downslope Index")
tool_labels.append("Drainage Preserving Smoothing")
tool_labels.append("Edge Density")
tool_labels.append("Edge Preserving Mean Filter")
tool_labels.append("Edge Proportion")
tool_labels.append("Elev Above Pit")
tool_labels.append("Elev Percentile")
tool_labels.append("Elev Relative To Min Max")
tool_labels.append("Elev Relative To Watershed Min Max")
tool_labels.append("Elevation Above Stream")
tool_labels.append("Elevation Above Stream Euclidean")
tool_labels.append("Eliminate Coincident Points")
tool_labels.append("Elongation Ratio")
tool_labels.append("Emboss Filter")
tool_labels.append("Equal To")
tool_labels.append("Erase")
tool_labels.append("Erase Polygon From Lidar")
tool_labels.append("Erase Polygon From Raster")
tool_labels.append("Euclidean Allocation")
tool_labels.append("Euclidean Distance")
tool_labels.append("Exp")
tool_labels.append("Exp2")
tool_labels.append("Export Table To Csv")
tool_labels.append("Extend Vector Lines")
tool_labels.append("Extract Nodes")
tool_labels.append("Extract Raster Statistics")
tool_labels.append("Extract Raster Values At Points")
tool_labels.append("Extract Streams")
tool_labels.append("Extract Valleys")
tool_labels.append("Farthest Channel Head")
tool_labels.append("Fast Almost Gaussian Filter")
tool_labels.append("Fd8 Flow Accumulation")
tool_labels.append("Fd8 Pointer")
tool_labels.append("Feature Preserving Denoise")
tool_labels.append("Fetch Analysis")
tool_labels.append("Fill Burn")
tool_labels.append("Fill Depressions")
tool_labels.append("Fill Missing Data")
tool_labels.append("Fill Single Cell Pits")
tool_labels.append("Filter Lidar Scan Angles")
tool_labels.append("Find Flightline Edge Points")
tool_labels.append("Find Lowest Or Highest Points")
tool_labels.append("Find Main Stem")
tool_labels.append("Find No Flow Cells")
tool_labels.append("Find Parallel Flow")
tool_labels.append("Find Patch Or Class Edge Cells")
tool_labels.append("Find Ridges")
tool_labels.append("Flatten Lakes")
tool_labels.append("Flightline Overlap")
tool_labels.append("Flip Image")
tool_labels.append("Flood Order")
tool_labels.append("Floor")
tool_labels.append("Flow Accumulation Full Workflow")
tool_labels.append("Flow Length Diff")
tool_labels.append("Gamma Correction")
tool_labels.append("Gaussian Contrast Stretch")
tool_labels.append("Gaussian Filter")
tool_labels.append("Greater Than")
tool_labels.append("Hack Stream Order")
tool_labels.append("High Pass Filter")
tool_labels.append("High Pass Median Filter")
tool_labels.append("Highest Position")
tool_labels.append("Hillshade")
tool_labels.append("Hillslopes")
tool_labels.append("Histogram Equalization")
tool_labels.append("Histogram Matching")
tool_labels.append("Histogram Matching Two Images")
tool_labels.append("Hole Proportion")
tool_labels.append("Horizon Angle")
tool_labels.append("Horton Stream Order")
tool_labels.append("Hypsometric Analysis")
tool_labels.append("Idw Interpolation")
tool_labels.append("Ihs To Rgb")
tool_labels.append("Image Autocorrelation")
tool_labels.append("Image Correlation")
tool_labels.append("Image Regression")
tool_labels.append("Image Stack Profile")
tool_labels.append("Impoundment Size Index")
tool_labels.append("In Place Add")
tool_labels.append("In Place Divide")
tool_labels.append("In Place Multiply")
tool_labels.append("In Place Subtract")
tool_labels.append("Increment")
tool_labels.append("Integer Division")
tool_labels.append("Integral Image")
tool_labels.append("Intersect")
tool_labels.append("Is No Data")
tool_labels.append("Isobasins")
tool_labels.append("Jenson Snap Pour Points")
tool_labels.append("Join Tables")
tool_labels.append("K Means Clustering")
tool_labels.append("K Nearest Mean Filter")
tool_labels.append("Kappa Index")
tool_labels.append("Ks Test For Normality")
tool_labels.append("Laplacian Filter")
tool_labels.append("Laplacian Of Gaussian Filter")
tool_labels.append("Las To Ascii")
tool_labels.append("Las To Multipoint Shapefile")
tool_labels.append("Las To Shapefile")
tool_labels.append("Layer Footprint")
tool_labels.append("Lee Filter")
tool_labels.append("Length Of Upstream Channels")
tool_labels.append("Less Than")
tool_labels.append("Lidar Block Maximum")
tool_labels.append("Lidar Block Minimum")
tool_labels.append("Lidar Classify Subset")
tool_labels.append("Lidar Colourize")
tool_labels.append("Lidar Construct Vector Tin")
tool_labels.append("Lidar Elevation Slice")
tool_labels.append("Lidar Ground Point Filter")
tool_labels.append("Lidar Hex Binning")
tool_labels.append("Lidar Hillshade")
tool_labels.append("Lidar Histogram")
tool_labels.append("Lidar Idw Interpolation")
tool_labels.append("Lidar Info")
tool_labels.append("Lidar Join")
tool_labels.append("Lidar Kappa Index")
tool_labels.append("Lidar Nearest Neighbour Gridding")
tool_labels.append("Lidar Point Density")
tool_labels.append("Lidar Point Stats")
tool_labels.append("Lidar Remove Duplicates")
tool_labels.append("Lidar Remove Outliers")
tool_labels.append("Lidar Segmentation")
tool_labels.append("Lidar Segmentation Based Filter")
tool_labels.append("Lidar Thin")
tool_labels.append("Lidar Thin High Density")
tool_labels.append("Lidar Tile")
tool_labels.append("Lidar Tile Footprint")
tool_labels.append("Lidar Tin Gridding")
tool_labels.append("Lidar Tophat Transform")
tool_labels.append("Line Detection Filter")
tool_labels.append("Line Intersections")
tool_labels.append("Line Thinning")
tool_labels.append("Linearity Index")
tool_labels.append("Lines To Polygons")
tool_labels.append("List Unique Values")
tool_labels.append("Ln")
tool_labels.append("Log10")
tool_labels.append("Log2")
tool_labels.append("Long Profile")
tool_labels.append("Long Profile From Points")
tool_labels.append("Longest Flowpath")
tool_labels.append("Lowest Position")
tool_labels.append("Majority Filter")
tool_labels.append("Max")
tool_labels.append("Max Absolute Overlay")
tool_labels.append("Max Anisotropy Dev")
tool_labels.append("Max Anisotropy Dev Signature")
tool_labels.append("Max Branch Length")
tool_labels.append("Max Difference From Mean")
tool_labels.append("Max Downslope Elev Change")
tool_labels.append("Max Elev Dev Signature")
tool_labels.append("Max Elevation Deviation")
tool_labels.append("Max Overlay")
tool_labels.append("Max Upslope Flowpath Length")
tool_labels.append("Maximum Filter")
tool_labels.append("Mean Filter")
tool_labels.append("Median Filter")
tool_labels.append("Medoid")
tool_labels.append("Merge Table With Csv")
tool_labels.append("Merge Vectors")
tool_labels.append("Min")
tool_labels.append("Min Absolute Overlay")
tool_labels.append("Min Downslope Elev Change")
tool_labels.append("Min Max Contrast Stretch")
tool_labels.append("Min Overlay")
tool_labels.append("Minimum Bounding Box")
tool_labels.append("Minimum Bounding Circle")
tool_labels.append("Minimum Bounding Envelope")
tool_labels.append("Minimum Convex Hull")
tool_labels.append("Minimum Filter")
tool_labels.append("Modified K Means Clustering")
tool_labels.append("Modulo")
tool_labels.append("Mosaic")
tool_labels.append("Mosaic With Feathering")
tool_labels.append("Multi Part To Single Part")
tool_labels.append("Multiply")
tool_labels.append("Multiscale Roughness")
tool_labels.append("Multiscale Roughness Signature")
tool_labels.append("Multiscale Topographic Position Image")
tool_labels.append("Nearest Neighbour Gridding")
tool_labels.append("Negate")
tool_labels.append("New Raster From Base")
tool_labels.append("Normal Vectors")
tool_labels.append("Normalized Difference Vegetation Index")
tool_labels.append("Not")
tool_labels.append("Not Equal To")
tool_labels.append("Num Downslope Neighbours")
tool_labels.append("Num Inflowing Neighbours")
tool_labels.append("Num Upslope Neighbours")
tool_labels.append("Olympic Filter")
tool_labels.append("Opening")
tool_labels.append("Or")
tool_labels.append("Panchromatic Sharpening")
tool_labels.append("Patch Orientation")
tool_labels.append("Pennock Landform Class")
tool_labels.append("Percent Elev Range")
tool_labels.append("Percent Equal To")
tool_labels.append("Percent Greater Than")
tool_labels.append("Percent Less Than")
tool_labels.append("Percentage Contrast Stretch")
tool_labels.append("Percentile Filter")
tool_labels.append("Perimeter Area Ratio")
tool_labels.append("Pick From List")
tool_labels.append("Plan Curvature")
tool_labels.append("Polygon Area")
tool_labels.append("Polygon Long Axis")
tool_labels.append("Polygon Perimeter")
tool_labels.append("Polygon Short Axis")
tool_labels.append("Polygonize")
tool_labels.append("Polygons To Lines")
tool_labels.append("Power")
tool_labels.append("Prewitt Filter")
tool_labels.append("Principal Component Analysis")
tool_labels.append("Print Geo Tiff Tags")
tool_labels.append("Profile")
tool_labels.append("Profile Curvature")
tool_labels.append("Quantiles")
tool_labels.append("Radius Of Gyration")
tool_labels.append("Raise Walls")
tool_labels.append("Random Field")
tool_labels.append("Random Sample")
tool_labels.append("Range Filter")
tool_labels.append("Raster Area")
tool_labels.append("Raster Cell Assignment")
tool_labels.append("Raster Histogram")
tool_labels.append("Raster Streams To Vector")
tool_labels.append("Raster Summary Stats")
tool_labels.append("Raster To Vector Lines")
tool_labels.append("Raster To Vector Points")
tool_labels.append("Rasterize Streams")
tool_labels.append("Reciprocal")
tool_labels.append("Reclass")
tool_labels.append("Reclass Equal Interval")
tool_labels.append("Reclass From File")
tool_labels.append("Reinitialize Attribute Table")
tool_labels.append("Related Circumscribing Circle")
tool_labels.append("Relative Aspect")
tool_labels.append("Relative Stream Power Index")
tool_labels.append("Relative Topographic Position")
tool_labels.append("Remove Off Terrain Objects")
tool_labels.append("Remove Polygon Holes")
tool_labels.append("Remove Short Streams")
tool_labels.append("Remove Spurs")
tool_labels.append("Resample")
tool_labels.append("Rescale Value Range")
tool_labels.append("Rgb To Ihs")
tool_labels.append("Rho8 Pointer")
tool_labels.append("Roberts Cross Filter")
tool_labels.append("Root Mean Square Error")
tool_labels.append("Round")
tool_labels.append("Ruggedness Index")
tool_labels.append("Scharr Filter")
tool_labels.append("Sediment Transport Index")
tool_labels.append("Select Tiles By Polygon")
tool_labels.append("Set Nodata Value")
tool_labels.append("Shape Complexity Index")
tool_labels.append("Shreve Stream Magnitude")
tool_labels.append("Sigmoidal Contrast Stretch")
tool_labels.append("Sin")
tool_labels.append("Single Part To Multi Part")
tool_labels.append("Sinh")
tool_labels.append("Sink")
tool_labels.append("Slope")
tool_labels.append("Slope Vs Elevation Plot")
tool_labels.append("Smooth Vectors")
tool_labels.append("Snap Pour Points")
tool_labels.append("Sobel Filter")
tool_labels.append("Split Colour Composite")
tool_labels.append("Split With Lines")
tool_labels.append("Square")
tool_labels.append("Square Root")
tool_labels.append("Standard Deviation Contrast Stretch")
tool_labels.append("Standard Deviation Filter")
tool_labels.append("Standard Deviation Of Slope")
tool_labels.append("Stochastic Depression Analysis")
tool_labels.append("Strahler Order Basins")
tool_labels.append("Strahler Stream Order")
tool_labels.append("Stream Link Class")
tool_labels.append("Stream Link Identifier")
tool_labels.append("Stream Link Length")
tool_labels.append("Stream Link Slope")
tool_labels.append("Stream Slope Continuous")
tool_labels.append("Subbasins")
tool_labels.append("Subtract")
tool_labels.append("Sum Overlay")
tool_labels.append("Surface Area Ratio")
tool_labels.append("Symmetrical Difference")
tool_labels.append("Tan")
tool_labels.append("Tangential Curvature")
tool_labels.append("Tanh")
tool_labels.append("Thicken Raster Line")
tool_labels.append("Tin Gridding")
tool_labels.append("To Degrees")
tool_labels.append("To Radians")
tool_labels.append("Tophat Transform")
tool_labels.append("Topological Stream Order")
tool_labels.append("Total Curvature")
tool_labels.append("Total Filter")
tool_labels.append("Trace Downslope Flowpaths")
tool_labels.append("Trend Surface")
tool_labels.append("Trend Surface Vector Points")
tool_labels.append("Tributary Identifier")
tool_labels.append("Truncate")
tool_labels.append("Turning Bands Simulation")
tool_labels.append("Union")
tool_labels.append("Unnest Basins")
tool_labels.append("Unsharp Masking")
tool_labels.append("User Defined Weights Filter")
tool_labels.append("Vector Hex Binning")
tool_labels.append("Vector Lines To Raster")
tool_labels.append("Vector Points To Raster")
tool_labels.append("Vector Polygons To Raster")
tool_labels.append("Viewshed")
tool_labels.append("Visibility Index")
tool_labels.append("Voronoi Diagram")
tool_labels.append("Watershed")
tool_labels.append("Weighted Overlay")
tool_labels.append("Weighted Sum")
tool_labels.append("Wetness Index")
tool_labels.append("Write Function Memory Insertion")
tool_labels.append("Xor")
tool_labels.append("Z Scores")


