# -*- coding: utf-8 -*-
"""
geocode

geocode addresses from csv files
"""
import pandas as pd
pd.options.display.max_rows = 10
pd.options.display.precision = 2
import dask.dataframe as dd

dtypes = {'Address_Detail_PID': 'object','Street_Locality_PID': 'object',
         'Locality_PID': 'object','Building_Name': 'object',
         'Lot_Number_Prefix': 'object', 'Lot_Number': 'object',
         'Lot_Number_Suffix': 'object', 'Flat_Type': 'object',
         'Flat_Number_Prefix': 'object', 'Flat_Number': 'object',
         'Flat_Number_Suffix': 'object', 'Level_Type': 'object',
         'Level_Number': 'object', 'Number_First_Prefix': 'object',
         'Number_First': 'object', 'Street_Name': 'object',
         'Street_Type_Code': 'object', 'Locality_Name': 'object',
         'State_Abbreviation': 'object', 'Postcode': 'object',
         'Confidence': 'int64', 'AddressText': 'object', 'Latitude': 'float64',
         'Longitude': 'float64','Geocode_Type': 'object'}

gnaf_df = dd.read_csv("gnaf_feb_2020_address_view.csv",dtype=dtypes)
search_df = dd.read_csv("addresses_cleaned.txt", header=None)

def bulk_geocode(search_df, gnaf_df):
    df_is_empty = {'Address_Detail_PID': [''],'Street_Locality_PID': [''],
         'Locality_PID': [''],'Building_Name': [''], 'Lot_Number_Prefix': [''],
         'Lot_Number': [''], 'Lot_Number_Suffix': [''], 'Flat_Type': [''],
         'Flat_Number_Prefix': [''], 'Flat_Number': [''], 
         'Flat_Number_Suffix': [''], 'Level_Type': [''], 'Level_Number': [''],
         'Number_First_Prefix': [''],'Number_First': [0], 'Street_Name': [''],
         'Street_Type_Code': [''], 'Locality_Name': [''], 
         'State_Abbreviation': [''],'Postcode': [''], 'Confidence': [0],
         'AddressText': [''], 'Latitude': [0.0], 'Longitude': [0.0], 
         'Geocode_Type': ['']}
    results_geocode_df = pd.DataFrame([])
    for i, val in search_df.iterrows():
        print('Processing record:',i+1,'address:',val[0])
        g_res = gnaf_df[gnaf_df.AddressText.str.contains(pat=val[0])].compute()
        try:
            out_df = g_res.iloc[0]
            print('address found by pattern')
        except IndexError:
            out_df = pd.DataFrame.from_dict(df_is_empty)
            print('address not found')
        #print(out_df)
        results_geocode_df = results_geocode_df.append(out_df)
        #results_geocode.append(out)
    #print(results_geocode_df)
    return results_geocode_df



processed_df = bulk_geocode(search_df, gnaf_df)
print('*done*')
processed_df.to_csv("addressed_processed.csv",index=False)

