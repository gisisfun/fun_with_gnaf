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
from sqlalchemy import create_engine, MetaData,Table, select,and_
import geopandas as gpd
from shapely.geometry import Point

import math, numpy as np

def get_bearing(lat1,lon1,lat2,lon2):
    dLon = lon2 - lon1;
    y = math.sin(dLon) * math.cos(lat2);
    x = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dLon);
    brng = np.rad2deg(math.atan2(y, x));
    if brng < 0: brng+= 360
    return brng

def read_poi(fname,tab=False):
    sep_char=','
    if tab:
        sep_char ='\t'
    df=pd.read_csv(fname,sep=sep_char)
    return df

def gnaf_agil():
    t_locality = Table('LOCALITY', metadata, autoload=True, 
                         autoload_with=engine)
    t_locality_point = Table('LOCALITY_POINT', metadata, autoload=True, 
                               autoload_with=engine)
    
    print('locality_point')
    print(t_locality_point.columns.keys())
    print('locality')
    print(t_locality.columns.keys())
    

    
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
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.longitude, df.latitude,))
    
    return gdf

def closest_addresses(v_stmt,row,tolerance = 1):
    v_address_view= Table('ADDRESS_TBL',metadata, autoload=True, 
                          autoload_with=engine)
    v_stmt_loop = v_stmt.where(
            and_(v_address_view.columns.Longitude.between(int(row.Longitude)-tolerance,
                                                          int(row.Longitude)+tolerance),
    v_address_view.columns.Latitude.between(int(row.Latitude)-tolerance,
                                            int(row.Latitude)+tolerance)))
    found = False
    print('* query to dataframe *')
    data=[]
    for result in connection.execute(v_stmt_loop):
    
    
    
        distance_km = geodesic((result.Latitude,result.Longitude),
                               (row.Latitude,row.Longitude)).km
                               
        data.append([result.Address_Detail_PID,result.AddressText.strip(),
                     result.Latitude,result.Longitude,
                     row.UCL_CODE_2016,row.UCL_NAME_2016,
                     row.Latitude,row.Longitude, distance_km])
        
    data_df=pd.DataFrame(data,columns=['Address_Detail_PID','AddressText',
                                             'address_latitude','address_longitude',
                                             'UCL_CODE_2016','UCL_NAME_2016',
                                             'locality_latitude',
                                             'locality_longitude','distance_km'])
    return data_df,found

def closest_address(v_stmt,row,tolerance = 1):
    v_address_view= Table('ADDRESS_TBL',metadata, autoload=True, 
                          autoload_with=engine)
    v_stmt_loop = v_stmt.where(
            and_(v_address_view.columns.Longitude.between(int(row.Longitude)-tolerance,
                                                          int(row.Longitude)+tolerance),
    v_address_view.columns.Latitude.between(int(row.Latitude)-tolerance,
                                            int(row.Latitude)+tolerance)))
    found = False
    small_data = ['0', 0, 0, 0, row.UCL_CODE_2016,\
                row.UCL_NAME_2016,row.Latitude, row.Longitude,0]
    smallest=99999
    for result in connection.execute(v_stmt_loop):
        distance_km=geodesic((result.Latitude,result.Longitude), 
                             (row.Latitude,row.Longitude)).km
        #if distance_km < 60:

        if distance_km < smallest:
            smallest=distance_km
            small_data=[result.Address_Detail_PID,result.AddressText.strip(),
                        result.Latitude,result.Longitude, row.UCL_CODE_2016,
                        row.UCL_NAME_2016,row.Latitude, row.Longitude,
                        distance_km]
            found = True
    return small_data, found

def get_agil():
    agil_names_url="https://data.gov.au/data/dataset/34b1c164-fbe8-44a0-84fd-467dba645aa7/resource/6947c036-6383-44f3-a867-0fa0c2a48d6b/download/agil_names20190208.csv"
    agil_locations_url="https://data.gov.au/data/dataset/34b1c164-fbe8-44a0-84fd-467dba645aa7/resource/625e0a41-6a30-4c11-9a20-ac64ba5a1d1f/download/agil_locations20190208.csv"
    agil_names = pd.read_csv(agil_names_url)
    agil_locations = pd.read_csv(agil_locations_url)
    agil_joined = pd.merge(agil_locations,agil_names,on='LCODE')
    geom=[Point(xy) for xy in zip(agil_joined.LONGITUDE, agil_joined.LATITUDE)]
    agil_joined_gdf=gpd.GeoDataFrame(agil_joined,geometry=geom,crs="EPSG:4283")
    return agil_joined_gdf

def add_cols(df,id_col,id_name):
    rafile = gpd.read_file('shape/RA_2016_AUST.shp')
    rafile['RA_NAME16'] = rafile['RA_NAME16'].str.replace('.\(.*\)','')
    
    geom=[Point(xy) for xy in zip(df.locality_longitude, df.locality_latitude)]
    df_poi_gdf=gpd.GeoDataFrame(df[['Address_Detail_PID',
                                    'locality_latitude', 
                                    'locality_longitude']], geometry = geom, crs = "EPSG:4283")
    df_poi_ra_gdf = gpd.sjoin(df_poi_gdf, rafile[['RA_NAME16','geometry']][rafile.geometry!=None], how='left', op='within')
    df_poi_ra = df_poi_ra_gdf.drop(columns=['geometry','index_right','locality_latitude', 'locality_longitude'])
    df_poi_ra.columns = ['Address_Detail_PID', 'locality_longlat_RA16']
    
    geom=[Point(xy) for xy in zip(df.address_longitude, df.address_latitude)]
    df_address_gdf=gpd.GeoDataFrame(df,geometry=geom,crs="EPSG:4283")
    
    df_address_ra_gdf = gpd.sjoin(df_address_gdf, rafile[['RA_NAME16','geometry']][rafile.geometry!=None], how='left', op='within')
    df_address_ra_gdf.rename(columns={'RA_NAME16': 'address_longlat_RA16'}, inplace=True)
    
    df_out = pd.merge(df_address_ra_gdf[['Address_Detail_PID', 'AddressText', 'address_latitude',
           'address_longitude', id_col, id_name,
           'locality_latitude', 'locality_longitude', 'distance_km','address_longlat_RA16']],df_poi_ra,on='Address_Detail_PID')
    df_out['RA16_Diff_Flag'] = df_out['address_longlat_RA16'] != df_out['locality_longlat_RA16']
    df_out['RA16_Diff_Flag'] = df_out.RA16_Diff_Flag.apply(lambda x:int(x))
    df_out= df_out.drop_duplicates(id_col)
    return df_out

def post_agil():
    agil_names_url="https://data.gov.au/data/dataset/34b1c164-fbe8-44a0-84fd-467dba645aa7/resource/6947c036-6383-44f3-a867-0fa0c2a48d6b/download/agil_names20190208.csv"
    agil_locations_url="https://data.gov.au/data/dataset/34b1c164-fbe8-44a0-84fd-467dba645aa7/resource/625e0a41-6a30-4c11-9a20-ac64ba5a1d1f/download/agil_locations20190208.csv"



    agil_names = pd.read_csv(agil_names_url)
    agil_locations = pd.read_csv(agil_locations_url)
    agil_joined = pd.merge(agil_locations,agil_names,on='LCODE')
    geom=[Point(xy) for xy in zip(agil_joined.LONGITUDE, agil_joined.LATITUDE)]
    agil_joined_gdf=gpd.GeoDataFrame(agil_joined,geometry=geom,crs="EPSG:4283")
    rafile = gpd.read_file('shape/RA_2016_AUST.shp')
    agil_remote_gdf = gpd.sjoin(agil_joined_gdf, rafile[['RA_NAME16','geometry']][rafile.geometry!=None], how='left', op='within')
    p_agil = agil_remote_gdf.loc[agil_remote_gdf['NFLAG']=='P',['LCODE','NAME','STATE','LONGITUDE','LATITUDE','RA_NAME16']]
    a_agil = agil_remote_gdf[agil_remote_gdf.NFLAG=='A']
    
    
    # stages 1 and 2 - convert to inputs to geospatial and base process
    ref_agil= pd.merge(df_closest, p_agil, left_on='locality_name', right_on='NAME', 
                       how='left')
    ref_agil['locality_longlat_RA16'] = ref_agil.RA_NAME16.str.replace('.\(.*\)','')
    process_dataset_1 = ref_agil[['LCODE','locality_pid','locality_name','locality_latitude',
                         'locality_longitude','locality_longlat_RA16','distance_km',
                         'Address_Detail_PID','AddressText','address_latitude',
                         'address_longitude']]
    
    geom=[Point(xy) for xy in zip(process_dataset_1.address_longitude, 
          process_dataset_1.address_latitude)]
    process_dataset_1_gdf = gpd.GeoDataFrame(process_dataset_1,geometry=geom,
                                      crs="EPSG:4283")
    process_dataset_2_gdf = gpd.sjoin(process_dataset_1_gdf, 
                                rafile[['RA_NAME16','geometry']][rafile.geometry!=None], 
                                how='left', op='within')
    process_dataset_2_gdf['AddressText'] = process_dataset_2_gdf.AddressText.str.strip()
    
    
    process_dataset_2_gdf['RA16_Diff_Flag'] = process_dataset_2_gdf['address_longlat_RA16'] != process_dataset_2_gdf['locality_longlat_RA16']
    process_dataset_2_gdf['RA16_Diff_Flag'] = process_dataset_2_gdf.RA16_Diff_Flag.apply(lambda x:int(x))
    
    #stage 3 - drop working columns and output primary list
    process_dataset_3 = process_dataset_2_gdf.drop(['geometry','index_right','RA_NAME16'], axis = 1)
    
    process_dataset_3.to_csv('csv/new_closest_wout_alts.csv')
    agil_joined_ref = process_dataset_3[['LCODE','NCODE','NAME','NFLAG']]
    
    #stage 4 and 5 - replace with alternate name references and output complete list
    process_dataset_4 = pd.merge(process_dataset_3, agil_joined_ref, on='LCODE', 
                       how='left')
    process_dataset_4['locality_name'] = process_dataset_4.NAME
    process_dataset_5 = process_dataset_4.drop(['NCODE','NFLAG','NAME'],axis=1)
    #process_dataset_5 = process_dataset_4.drop(['NCODE','NAME'],axis=1)
    
    process_dataset_5.to_csv('csv/new_closest_w_alts.csv')

def mb_aust():
    mbact = gpd.read_file('shape/MB_2016_ACT.shp')
    mbnsw = gpd.read_file('shape/MB_2016_NSW.shp')
    mbnt = gpd.read_file('shape/MB_2016_NT.shp')
    mbot = gpd.read_file('shape/MB_2016_OT.shp')
    mbqld = gpd.read_file('shape/MB_2016_QLD.shp')
    mbsa = gpd.read_file('shape/MB_2016_SA.shp')
    mbtas = gpd.read_file('shape/MB_2016_TAS.shp')
    mbvic = gpd.read_file('shape/MB_2016_VIC.shp')
    mbwa = gpd.read_file('shape/MB_2016_WA.shp')
    gdf = pd.concat([mbact, mbnsw, mbnt, mbnt, mbot, mbqld, mbsa, mbtas, mbvic, 
                     mbwa])
    gdf.STE_NAME16.astype('category').unique()
    return gdf 


engine = create_engine('sqlite:///spatialite_db/gnaf_may_2020_new.sqlite')
print(engine.table_names())
connection = engine.connect()
#tables
metadata = MetaData()
#ADDRESS_DETAIL ->  ADDRESS_DETAIL_PID (in v_address_view)
#ADDRESS_MESH_BLOCK_2016 -> ADDRESS_MESH_BLOCK_2016_PID,ADDRESS_DETAIL_PID,MB_2016_PID
#MB_2016 -> MB_2016_PID,MB_2016_CODE

print('address view')
v_address_view= Table('ADDRESS_TBL',metadata, autoload=True, 
                       autoload_with=engine)
print(v_address_view.columns.keys())

v_address_view= Table('ADDRESS_TBL',metadata, autoload=True, 
                           autoload_with=engine)
closest=[]
test=read_poi('csv/ucl.txt',tab=True)
df=test[test.Latitude!=0]
v_stmt = select([v_address_view.columns.Address_Detail_PID,
v_address_view.columns.Latitude, v_address_view.columns.Longitude,
v_address_view.columns.AddressText])
##
for index,row in df.iterrows():
    #limit by bounding box
    tolerance = 1

    while True:
        print('trying tolerance', tolerance,' degree and row \n',row)
        small_data, found = closest_address(v_stmt,row,tolerance)
        print(index,small_data)
        if found == True:
            break
        else:
            tolerance += 1 
 
    
    closest.append(small_data)


connection.close()
print(closest)

df_closest=pd.DataFrame(closest,columns=['Address_Detail_PID','AddressText',
                                         'address_latitude','address_longitude',
                                         'UCL_CODE_2016','UCL_NAME_2016',
                                         'locality_latitude',
                                         'locality_longitude','distance_km'])
df_closest.to_csv('closest3.csv')
    
    
    
    
#df_closest = read_poi('closest3.csv')
df_out = add_cols(df_closest,'UCL_CODE_2016','UCL_NAME_2016')


