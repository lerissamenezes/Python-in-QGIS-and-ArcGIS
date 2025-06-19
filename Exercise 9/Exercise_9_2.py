#9.2

import arcpy

# path to geodata
arcpy.env.workspace = r"C:\Users\hp\Desktop\Python in QGIS and ArcGIS\Exercises\Exercise 9\exercise_arcpy_1.gdb"
arcpy.env.overwriteOutput = True

# selecting features to be working with
input_fc = "active_assets"
buffer_fc = "coverage"

# Adding a helper field to store buffer distance
distance_field = "buffer_dist"
if distance_field not in [f.name for f in arcpy.ListFields(input_fc)]:
    arcpy.AddField_management(input_fc, distance_field, "DOUBLE")

# Calculating field values based on 'type'
# Buffer distances:
# - mast: 300
# - mobile_antenna: 50
# - building_antenna: 100

expression = """def calc_dist(type):
    if type == 'mast':
        return 300
    elif type == 'mobile_antenna':
        return 50
    elif type == 'building_antenna':
        return 100
    else:
        return 0
"""
arcpy.CalculateField_management(
    in_table=input_fc,
    field=distance_field,
    expression="calc_dist(!type!)",
    code_block=expression,
    expression_type="PYTHON3"
)

# Creating buffer using the helper field
arcpy.Buffer_analysis(
    in_features=input_fc,
    out_feature_class=buffer_fc,
    buffer_distance_or_field=distance_field,
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="ALL",  # Optional: use "NONE" if you want individual buffers
    dissolve_field=None
)

print(f"Buffer analysis completed. Output feature class: {buffer_fc}")

#creating 3 layers with SQL
arcpy.management.MakeFeatureLayer("active_assets","layer_mast","type = 'mast'")
arcpy.management.MakeFeatureLayer("active_assets","layer_mobile","type = 'mobile_antenna'")
arcpy.management.MakeFeatureLayer("active_assets","layer_building","type = 'building_antenna'")

# Creating buffer using the helper field
arcpy.analysis.Buffer("layer_mast", "buffer_mast", "300 Meters")
arcpy.analysis.Buffer("layer_mobile", "buffer_mobile", "50 Meters")
arcpy.analysis.Buffer("layer_building", "buffer_building", "100 Meters")

#Merged output
arcpy.management.Merge(["buffer_mast","buffer_mobile","buffer_building"],"merged")
op="merged"
print(f"Buffer analysis completed. Output feature class: {op}")