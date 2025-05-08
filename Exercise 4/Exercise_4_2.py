import csv

# Get the active layer (assuming the "Schools" layer is active in QGIS)
# Get the active layer (make sure it's 'Schools')
layer = iface.activeLayer()

# Open the CSV file to write 
with open("C:/Users/hp/Desktop/SchoolReport.csv", "w", newline="", encoding="utf-8") as file:
    # Write the header
    file.write("NAME,X,Y\n")
    
    # Loop through only selected features
    for feature in layer.selectedFeatures():
        name = feature["NAME"]  # Replace with exact field name if different
        geom = feature.geometry()
        point = geom.asPoint()  # If it's a Point geometry

        x = point.x()
        y = point.y()

        # Write one line to CSV
        file.write(f"{name},{x},{y}\n")

#checking if the data has been written successfully        
print("Data has been written to SchoolReport.csv")