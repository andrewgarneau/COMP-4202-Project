import osmnx as ox
import networkx as nx
import geonetworkx as gnx
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from shapely.ops import nearest_points

def conv_longlat_to_pt(long: float, lat:float, name:str) -> gpd.GeoDataFrame:

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

def nearestAsJson(df1, df2, geom1_col='geometry', geom2_col='geometry', df2_column=None):
    # df1['nearest_id'] = df1.apply(_nearestHelper, df1=df1, df2=df2, geom1=geom1_col, geom2=geom2_col, df2_column=df2_column, axis=1)

    # output = df2.iloc[df1['nearest_id']]
    # print(output)

    return nearest(df1, df2, geom1_col, geom2_col, df2_column).to_json()

def nearest(df1, df2, geom1_col='geometry', geom2_col='geometry', df2_column=None):
    df1['nearest_id'] = df1.apply(_nearestHelper, df1=df1, df2=df2, geom1=geom1_col, geom2=geom2_col, df2_column=df2_column, axis=1)

    output = df2.iloc[df1['nearest_id']]

    return output

def get_nearest_repair_stand_json(x: float, y: float):
    pt = conv_longlat_to_pt(x, y, "Your location")
    nearest_rs = nearestAsJson(df1=pt, df2=repair_stands, df2_column=None)
    return nearest_rs

def get_nearest_repair_stand(x: float, y: float):
    pt = conv_longlat_to_pt(x, y, "Your location")
    nearest_rs = nearest(df1=pt, df2=repair_stands, df2_column=None)
    return nearest_rs

def get_route_to_nearest_repair_stand(x: float, y: float):
    origin = conv_longlat_to_pt(x, y, "origin").geometry.values[0]
    destination = get_nearest_repair_stand(x, y).geometry.values[0]

    origin_xy = (origin.y, origin.x)
    destination_xy = (destination.y, destination.x)

    source_node = ox.get_nearest_node(graph, origin_xy)
    target_node = ox.get_nearest_node(graph, destination_xy)

    route = nx.shortest_path(G=graph, source=source_node, target=target_node, weight="length")

    shortest_path_graph:nx.MultiDiGraph = graph.subgraph(route)

    output_gdf = gnx.graph_edges_to_gdf(shortest_path_graph)

    print("route")
    print(route)

    print("subgraph")
    print(output_gdf.to_json())

    print(origin)

    origin_geo_json = {
        "type": "feature",
        "geometry": {
            "type": "Point",
            "coordinates": [origin.x, origin.y]
        },
        "properties": {
            "name": "Origin"
        }
    }

    destination_geo_json = {
        "type": "feature",
        "geometry": {
            "type": "Point",
            "coordinates": [destination.x, destination.y]
        },
        "properties": {
            "name": "Destination"
        }
    }

    return {
        "start": origin_geo_json,
        "end": destination_geo_json,
        "route": output_gdf.to_json()
    }



# network = gpd.read_file('geospatial_processing/sources/Cycling_Network/Cycling_Network.shp')
# network.plot()
# print(network)

repair_stands:gpd.GeoDataFrame = gpd.read_file('geospatial_processing/sources/Bike_Repair_Stations/Bike_Repair_Stations.shp')

place_name = "Nepean, Ottawa, Canada"
graph = ox.graph_from_place(place_name)

res = get_route_to_nearest_repair_stand(-75.76992997643495, 45.34365181227424)
print("\n\n\nres:")
print(res)

print("Done loading GeoDataFrame")

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