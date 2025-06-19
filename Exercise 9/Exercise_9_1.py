#9.1

import arcpy
import os

# path to geodata
arcpy.env.workspace = r"C:\Users\hp\Desktop\Python in QGIS and ArcGIS\Exercises\Exercise 9\exercise_arcpy_1.gdb"
arcpy.env.overwriteOutput = True

# output feature class
output_fc = "active_assets"

# Creating the output feature class with the same schema as the first input one
if arcpy.Exists(output_fc):
    arcpy.Delete_management(output_fc)

# fetching all feature classes
fcs = arcpy.ListFeatureClasses()

for fc in fcs:
    desc = arcpy.Describe(fc)
    
    # only process point geometries
    if desc.shapeType == "Point":
        fields = [f.name for f in arcpy.ListFields(fc) if f.editable]
        
        # using SearchCursor to filter active status
        with arcpy.da.SearchCursor(fc, fields + ["SHAPE@"]) as search_cursor:
            for row in search_cursor:
                status_index = fields.index("status") if "status" in fields else -1
                
                if status_index != -1 and str(row[status_index]).lower() == "active":
                    # Creating output
                    if not arcpy.Exists(output_fc):
                        spatial_ref = desc.spatialReference
                        arcpy.CreateFeatureclass_management(
                            arcpy.env.workspace,
                            output_fc,
                            "POINT",
                            template=fc,
                            spatial_reference=spatial_ref
                        )

                        insert_cursor = arcpy.da.InsertCursor(output_fc, fields + ["SHAPE@"])
                    
                    # inserting row
                    insert_cursor.insertRow(row)

# Check
try:
    insert_cursor
except NameError:
    print("No active point features found.")
else:
    del insert_cursor
    print("Done! Active assets copied to:", output_fc)
