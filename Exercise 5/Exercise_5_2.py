from qgis.PyQt.QtWidgets import QInputDialog
from qgis.core import QgsExpression, QgsFeatureRequest

# ask the user to enter an input
parent = iface.mainWindow()
canvas = iface.mapCanvas()
# This opens a text input dialog and save the input if the user pressed ok
sCoords, bOK = QInputDialog.getText(parent, "Coordinates", 
    "Enter coordinates as latitude, longitude", text=" ")
# only continue if the user pressed ok
if bOK:
    try:
        # it splits the input to lat and long by ,
        lat_str, lon_str = sCoords.split(",")
        # transforming the input string into float
        lat = float(lat_str.strip())
        lon = float(lon_str.strip())
    except Exception as e:
        QMessageBox.warning(parent, "Error", f"Invalid input format: {e}")

from qgis.core import (
    QgsPointXY, QgsCoordinateReferenceSystem,
    QgsCoordinateTransform, QgsProject, QgsGeometry
)

# setting the source and target reference systems
wgs84 = QgsCoordinateReferenceSystem("EPSG:4326")
etrs89 = QgsCoordinateReferenceSystem("EPSG:25832")

point_wgs84 = QgsPointXY(lon, lat)

# transforming between the two CRS
transformer = QgsCoordinateTransform(wgs84, etrs89, QgsProject.instance())
point_etrs89 = transformer.transform(point_wgs84)

# check if the point is inside any district
layer = QgsProject.instance().mapLayersByName("Muenster_City_Districts")[0]
# converts point to a geometry object
point_geom = QgsGeometry.fromPointXY(point_etrs89)
found = False
# loops through every feature and checks if it exists in the layer 
for feature in layer.getFeatures():
    if feature.geometry().contains(point_geom):
        found = True
        district_name = feature["Name"]  # or the actual field name
        break
 
 # show the results   
from PyQt5.QtWidgets import QMessageBox

if found:
    layer.removeSelection()
    QMessageBox.information(parent, "Result", f"The point is inside {district_name}.")
    layer.selectByIds([feature.id()])
    canvas.zoomToSelected(layer)
    
else:
    QMessageBox.information(parent, "Result", "The point is NOT inside any district of Muenster")