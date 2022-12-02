import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
from geopython import conv_longlat_to_pt, get_nearest_repair_stand
from pyrosm import OSM, get_data
import time

# get the map data from openstreetmap
place_name = "Nepean, Ottawa, Canada"
# place_name = "Ottawa, Ontario, Canada"
# # another way to get the graph is to use osmnx to get it but it's slow.
start_time = time.time()
graph = ox.graph_from_place(place_name)
print("--- %s seconds for getting the graph ---\n" % (time.time() - start_time))

# start_time = time.time()
# osm = OSM("geospatial_processing/sources/ncr.osm.pbf")
# nodes, edges = osm.get_network(nodes=True, network_type="cycling")
# print("--- %s seconds for getting the network ---\n" % (time.time() - start_time))
# start_time = time.time()
# graph = osm.to_graph(nodes,edges, graph_type="networkx")
# print("--- %s seconds for buidling the graph ---\n" % (time.time() - start_time))

# print(f"Type is {type(graph)}")

# fig, ax = ox.plot_graph(graph)
# plt.tight_layout()

area = ox.geocode_to_gdf(place_name)

# # adding this, shows buildings but it's uneccessary for this task.
# buildings = ox.geometries_from_place(place_name, tags={"building":True})

nodes_vis, edges_vis = ox.graph_to_gdfs(graph)
fig, ax = plt.subplots(1)

# fig, ax = ox.plot_graph(graph)
area.plot(ax=ax, facecolor='black')
edges_vis.plot(ax=ax, linewidth=1, edgecolor='#ADD8E6')

home_point = conv_longlat_to_pt(-75.76992997643495, 45.34365181227424, "Home").geometry.values[0]
home_point_xy = (home_point.y, home_point.x)

nearest_bike_stand = get_nearest_repair_stand(-75.76992997643495, 45.34365181227424).geometry.values[0]
nearest_bike_stand_xy = (nearest_bike_stand.y, nearest_bike_stand.x)

source_node = ox.get_nearest_node(graph, home_point_xy)
target_node = ox.get_nearest_node(graph, nearest_bike_stand_xy)

print("Source node:")
print(source_node)
print("Target node:")
print(target_node)

route = nx.shortest_path(G=graph, source=source_node, target=target_node, weight="length")
print("route", route)

# fig, ax = ox.plot_graph_route(graph, route, route_color='green', orig_dest_size=100)
ox.plot_graph_route(graph, route, route_color='green', route_alpha=1.0, orig_dest_size=100, ax=ax)


home_point.plot(ax=ax, color='red')
nearest_bike_stand.plot(ax=ax, color='red')

# buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)

print("done loading...")
plt.tight_layout()

plt.show()
