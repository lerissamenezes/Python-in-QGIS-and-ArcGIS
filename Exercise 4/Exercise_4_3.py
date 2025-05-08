# Import modules
import os
from qgis.core import QgsVectorLayer, QgsProject, QgsApplication

# Optional: Set QGIS install location if needed
# QgsApplication.setPrefixPath("C:/OSGeo4W/apps/qgis", True)

# Initialize QGIS Application (if running standalone)
qgs = QgsApplication([], False)
qgs.initQgis()

# Folder containing the shapefiles
folder_path = r"C:\Users\hp\Desktop\Python in QGIS and ArcGIS\Muenster"

# Output project path
project_output_path = r"C:\Users\hp\Desktop\Python in QGIS and ArcGIS\Exercises\Exercise 4\myfirstproject.qgz"

# Get all .shp files in the folder
shapefiles = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".shp")]

# Get project instance and clear any previous project
project = QgsProject.instance()
project.clear()

# Loop through all shapefiles and add valid layers
for shp_path in shapefiles:
    layer_name = os.path.splitext(os.path.basename(shp_path))[0]
    layer = QgsVectorLayer(shp_path, layer_name, "ogr")
    if layer.isValid():
        project.addMapLayer(layer)
        print(f"Added layer: {layer_name}")
    else:
        print(f"Invalid shapefile: {shp_path}")

# Save the project
project.write(project_output_path)
print(f"Project saved successfully to {project_output_path}")

# Exit QGIS app if needed
qgs.exitQgis()
