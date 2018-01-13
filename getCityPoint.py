import osmnx as ox
import csv
from geopandas import GeoDataFrame
from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon

ox.config(log_file=True, log_console=True, use_cache=True)

places = []
place_names = []
filename = 'cityList.csv'
with open(filename) as f:
    reader = csv.reader(f)
    places = list(reader)
for place in places:
    if(place[1] == 'yanbianzhou'):
        place_names.append('yanbian'+','+place[2]+','+place[3])
    elif(place[1] == 'daxinganlingdiqu'):
        place_names.append('daxinganling'+','+place[2]+','+place[3])
    else:
        place_names.append(place[1]+','+place[2]+','+place[3])

print(place_names)

dongSanSheng = ox.gdf_from_places(place_names, gdf_name='dongSanSheng_city')

print(dongSanSheng)


dongSanSheng_city_byPoint = GeoDataFrame([{'geometry':None,'place_name':None}])

for city_polygon,city_name,e,w,n,s in zip(dongSanSheng['geometry'],dongSanSheng['place_name'],dongSanSheng['bbox_east'],dongSanSheng['bbox_west'],dongSanSheng['bbox_north'],dongSanSheng['bbox_south']):
    placeName = city_name.split(',')[0]
    placeName = placeName.split('/')
    print(placeName)
    if len(placeName) > 1 and placeName[1].strip() == '白山市':
        placeName = '白山市'
    else:
        placeName = placeName[0].strip() 
    if isinstance(city_polygon, (Polygon, MultiPolygon)):
        x = (float(e) + float(w))/2
        y = (float(n) + float(s))/2
        city_point_df = GeoDataFrame([{'geometry' : Point(x, y).buffer(0.6)}])
        city_point_polygon = city_point_df['geometry'][0]
        print(placeName)
        dongSanSheng_city_byPoint = GeoDataFrame([{'place_name':placeName, 'geometry':city_point_polygon}])
        objectName = placeName + '坐标圆001'
        ox.save_gdf_shapefile(dongSanSheng_city_byPoint,filename=objectName, folder='osmnx_data/city/')
        filename1 = 'osmnx_data/city/'+objectName+'/'+placeName+'坐标圆001.shp'
        filename2 = 'osmnx_data/city/shp/'+placeName+'001.shp'
    elif isinstance(city_polygon, Point):
        city_point_df = GeoDataFrame([{'geometry' : city_polygon.buffer(0.6)}])
        city_point_polygon = city_point_df['geometry'][0]
        print(placeName)
        dongSanSheng_city_byPoint = GeoDataFrame([{'place_name':placeName, 'geometry':city_point_polygon}])
        objectName = placeName + '坐标圆001'
        ox.save_gdf_shapefile(dongSanSheng_city_byPoint,filename=objectName, folder='osmnx_data/city/')
        filename1 = 'osmnx_data/city/'+objectName+'/'+placeName+'坐标圆001.shp'
        filename2 = 'osmnx_data/city/shp/'+placeName+'001.shp'
    else:
        print('wrong datatype!')
