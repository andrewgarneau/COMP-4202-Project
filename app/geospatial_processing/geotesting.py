import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point
from geopython import conv_latlong_to_pt, get_nearest_repair_stand
from pyrosm import OSM, get_data
import time

home_point = conv_latlong_to_pt(-75.76992997643495, 45.34365181227424, "Home")
print(home_point.geometry.values[0])