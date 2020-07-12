#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:56:51 2020

@author: pi
"""
#import geopandas as gpd
#from shapely.geometry import Point
from geopy.distance import geodesic
import pandas as pd
from sqlalchemy import create_engine, MetaData,Table, select,and_,between

engine = create_engine('sqlite:///spatialite_db/gnaf_may_2020.sqlite')
print(engine.table_names())
connection = engine.connect()
#tables
metadata = MetaData()

t_locality = Table('LOCALITY', metadata, autoload=True, 
                     autoload_with=engine)
t_locality_point = Table('LOCALITY_POINT', metadata, autoload=True, 
                           autoload_with=engine)
v_address_view= Table('ADDRESS_VIEW',metadata, autoload=True, 
                           autoload_with=engine)
print('locality_point')
print(t_locality_point.columns.keys())
print('locality')
print(t_locality.columns.keys())

print('address view')
print(v_address_view.columns.keys())

ilocs_stmt = select([t_locality.columns.locality_pid,
               t_locality.columns.locality_name,
               t_locality.columns.state_pid,
               t_locality_point.columns.latitude,
               t_locality_point.columns.longitude,
               t_locality.columns.locality_class_code])
ilocs_stmt = ilocs_stmt.where(
        and_(t_locality.columns.locality_pid == t_locality_point.columns.locality_pid,
             t_locality.columns.locality_class_code == 'I'))
ilocs_stmt = ilocs_stmt.order_by(t_locality.columns.locality_pid)

results = connection.execute(ilocs_stmt).fetchall()
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()
#gdf = gpd.GeoDataFrame(
#    df, geometry=gpd.points_from_xy(df.longitude, df.latitude,))
# Print the DataFrame
print(df)
 
closest=[]

v_stmt = select([v_address_view.columns.Address_Detail_PID,
v_address_view.columns.Latitude, v_address_view.columns.Longitude,
v_address_view.columns.AddressText])
#
for index,row in df.iterrows():
    #limit by bounding box
    v_stmt_loop = v_stmt.where(
            and_(v_address_view.columns.Longitude.between(int(row.longitude)-2,
                                                          int(row.longitude)+2),
    v_address_view.columns.Latitude.between(int(row.latitude)-2,
                                            int(row.latitude)+2)))
    smallest=99999
    small_data=[0,0,0, 0,row.locality_pid,
                        row.locality_name,row.latitude, row.longitude,0]
    for result in connection.execute(v_stmt_loop):
        distance_km=geodesic((result.Latitude,result.Longitude), 
                             (row.latitude,row.longitude)).km
        #if distance_km < 60:

        if distance_km < smallest:
            smallest=distance_km
            small_data=[result.Address_Detail_PID,result.AddressText,
                        result.Latitude,result.Longitude, row.locality_pid,
                        row.locality_name,row.latitude, row.longitude,
                        distance_km]
    print(index,small_data)
    closest.append(small_data)


connection.close()
print(closest)

df_closest=pd.DataFrame(closest,columns=['Address_Detail_PID','AddressText',
                                         'address_latitude','address_longitude',
                                         'locality_pid','locality_name',
                                         'locality_latitude',
                                         'locality_longitude','distance_km'])
df_closest.to_csv('closest3.csv')
#geom=[Point(xy) for xy in zip([117.454361,117.459880],[38.8459879,38.846255])]
#gdf=gpd.GeoDataFrame(geometry=geom,crs={'init':'epsg:4326'})
