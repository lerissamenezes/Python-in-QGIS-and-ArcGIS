import processing

# Define input layers
polygon_layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]
point_layer = QgsProject.instance().mapLayersByName("Schools")[0]

# Run the 'Count points in polygon' tool
result = processing.run("native:countpointsinpolygon", {
    'POLYGONS': polygon_layer,
    'POINTS': point_layer,
    'FIELD': 'school_count',  # stores the counts
    'OUTPUT': 'memory:'  # Stores result in memory
})

# Get the resulting layer
output_layer = result['OUTPUT']

# Print the result
for feature in output_layer.getFeatures():
    name = feature['Name'] if 'Name' in feature.fields().names() else feature.attribute(0)  
    count = feature['school_count']
    print(f"{name}: {count}")
