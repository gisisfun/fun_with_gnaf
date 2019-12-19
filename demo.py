from gnaf.parameters import Tables,Defaults,DataSets,Scripts
from gnaf.thecode import Process

d = DataSets.gnaf_nov_2019.CSVFormat()

ds = Process.Do_Stuff('spatialite_db')

gnafP = d.PathToFiles
dbname = d.Description

ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_CHANGE_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.FLAT_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.GEOCODED_LEVEL_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.GEOCODE_RELIABILITY_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.GEOCODE_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.LEVEL_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.LOCALITY_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.LOCALITY_CLASS_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.MB_MATCH_CODE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.PS_JOIN_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_CLASS_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_SUFFIX_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_LOCALITY_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_TYPE_AUT(),gnafP,'Authority_Code/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_SUFFIX_AUT(),gnafP,'Authority_Code/'),dbname)

# Without Foreign key references
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_DETAIL(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_FEATURE(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.MB_2011(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.MB_2016(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STATE(),gnafP,'Standard/'),dbname)
# With Foreign key references
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_ALIAS(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_DEFAULT_GEOCODE(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_MESH_BLOCK_2011(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_MESH_BLOCK_2016(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_SITE(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_SITE_GEOCODE(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY_NEIGHBOUR(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.PRIMARY_SECONDARY(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY_POINT(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STREET_LOCALITY(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STREET_LOCALITY_ALIAS(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STREET_LOCALITY_POINT(),gnafP,'Standard/'),dbname)
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY_ALIAS(),gnafP,'Standard/'),dbname)

ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.LOCALITY_VIEW()),dbname)
ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.STREET_LOCALITY_VIEW()),dbname)
ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.ADDRESS_VIEW()),dbname)
ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.NEIGHBOUR_LOCALITY_VIEW()),dbname)
ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.NEIGHBOUR_LOCALITY_LIST_VIEW()),dbname)
ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.ALIAS_LOCALITY_VIEW()),dbname)
ds.sql_to_db(Process.Collate.create_views_sql_st(Tables.Views.SECONDARY_VIEW()),dbname)



print('extracting address view from database',d.Description)
s = Scripts.address_view()
ds.sql_to_db(s.Content.format(gnaf = d.Description),d.Description)

print('locality  view from database',d.Description)
s = Scripts.locality_view()
ds.sql_to_db(s.Content.format(gnaf = d.Description),d.Description)
