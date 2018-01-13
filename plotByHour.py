import osmnx as ox
from geopandas import GeoDataFrame
from shapely.geometry import Point
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from descartes import PolygonPatch
import csv

for i in range(12,22):
    fig, ax = plt.subplots(figsize=(6,6))

    placedf = GeoDataFrame.from_file('osmnx_data\province\province.shp')

    for geometry in placedf['geometry']:
        if isinstance(geometry, (Polygon, MultiPolygon)):
            if isinstance(geometry, Polygon):
                geometry = MultiPolygon([geometry])
            for polygon in geometry:
                print(polygon)
                patch = PolygonPatch(polygon, fc='#ffffff', ec='#555555', linewidth=1, alpha=1)
                ax.add_patch(patch)
        else:
            raise ValueError('All geometries in GeoDataFrame must be shapely Polygons or MultiPolygons')

    csv_reader = csv.reader(open('aqiData2018_1_2_'+ str(i) +'.csv', encoding='gb2312'))
    print(csv_reader)
    for city in csv_reader:
        if city[0] == 'city':
            continue
        city_name = city[0]
        if city_name == '延边州':
            city_name = '延边朝鲜族自治州'
        elif city_name != '大兴安岭地区':
            city_name = city_name + '市'

        print('city'+city_name)
        print('aqi'+city[1])

        if int(city[1])<20:
            color = '#eeeeee'
        elif int(city[1])< 30 :
            color = '#dddddd'
        elif int(city[1]) < 40 :
            color = '#cccccc'
        elif int(city[1]) < 50 :
            color = '#bbbbbb'
        elif int(city[1]) < 60:
            color = '#aaaaaa'
        elif int(city[1]) < 70:
            color = '#999999'
        elif int(city[1]) < 80:
            color = '#888888'
        elif int(city[1]) < 90:
            color = '#777777'
        elif int(city[1]) < 100:
            color = '#666666'
        elif int(city[1]) < 110:
            color = '#555555'
        elif int(city[1]) < 120:
            color = '#444444'
        elif int(city[1]) < 130:
            color = '#333333'
        elif int(city[1]) < 140:
            color = '#222222'
        elif int(city[1]) < 150:
            color = '#111111'
        else:
            color = '#000000'

        city_point_df = GeoDataFrame.from_file('osmnx_data/city/' + city_name+'坐标圆001/' +city_name+'坐标圆001.shp')
        polygon = city_point_df['geometry'][0]
        print(polygon)
        patch = PolygonPatch(polygon, fc=color, ec='#555555', linewidth=0, alpha=0.9)
        ax.add_patch(patch)

    # adjust the axis margins and limits around the image and make axes
    # equal-aspect
    margin = 0.02
    axis_off= True
    west, south, east, north = placedf.unary_union.bounds
    margin_ns = (north - south) * margin
    margin_ew = (east - west) * margin
    ax.set_ylim((south - margin_ns, north + margin_ns))
    ax.set_xlim((west - margin_ew, east + margin_ew))
    ax.set_aspect(aspect='equal', adjustable='box')
    if axis_off:
        ax.axis('off')
    # plt.show()
     
    ox.save_and_show(fig,ax,save = True,filename = 'city_point_pic/'+ str(i), show = False, close = True, file_format = 'png', dpi = 300 , axis_off = True)