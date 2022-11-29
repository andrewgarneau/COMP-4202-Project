import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.ops import nearest_points

print("hi")

def conv_latlong_to_pt(long: float, lat:float, name:str) -> gpd.GeoDataFrame:

    coordinates = [long, lat]
    point_coord = Point(coordinates)

    df = {"Location": [name], 'geometry':[point_coord]}

    point = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
    return point

def _nearestHelper(row, df1, df2, geom1='geometry', geom2='geometry', df2_column=None):

    union = df2.unary_union

    nearest = df2[geom2] == nearest_points(row[geom1], union)[1]

    if df2_column is None:
        value = df2[nearest].index[0]
    else:
        value = df2[nearest][df2_column].values[0]
    return value

def nearest(df1, df2, geom1_col='geometry', geom2_col='geometry', df2_column=None):
    df1['nearest_id'] = df1.apply(_nearestHelper, df1=df1, df2=df2, geom1=geom1_col, geom2=geom2_col, df2_column=df2_column, axis=1)

    output = df2.iloc[df1['nearest_id']]
    print(output)

    return output.to_json()

def get_nearest_repair_stand(x: float, y: float):
    pt = conv_latlong_to_pt(x, y, "Your location")
    nearest_rs = nearest(df1=pt, df2=repair_stands, df2_column=None)
    return nearest_rs

# network = gpd.read_file('geospatial_processing/sources/Cycling_Network/Cycling_Network.shp')
# network.plot()

repair_stands:gpd.GeoDataFrame = gpd.read_file('geospatial_processing/sources/Bike_Repair_Stations/Bike_Repair_Stations.shp')
# repair_stands.plot()

# fig, ax = plt.subplots(1)
# network.plot(ax=ax)
# repair_stands.plot(ax=ax,facecolor='red')

# my_house_point = conv_latlong_to_pt(-75.76992997643495, 45.34365181227424, "My House")
# my_house_point.plot()

# pt_nearest = nearest(df1=my_house_point, df2=repair_stands, df2_column=None)
# print("Nearest result:")
# print(pt_nearest)
# print(repair_stands.iloc[pt_nearest.nearest_id])

# print(my_house_point)
# print(repair_stands)

# plt.show()