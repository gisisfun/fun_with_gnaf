from gnaf.parameters import Tables,Defaults
from gnaf.thecode import Process
#d = Defaults()

#upd = 'UPDATE'
#
#print(p.sqlStart)
#
#    print(p.sqlState.format(state = thestate))
#    if thestate is not d.states8[-1]:
#        print(upd)
#    else:
#        print(';')
#for thestate in p.stateList:
#    print(thestate)
#    c.pipes_to_comma(p.filePiped.format(state = thestate))
#c.state_pipes(p)

#c = Process.Collect('AUG19_GNAF_PipeSeparatedValue/G-NAF_AUGUST_2019/','Standard/')
#c.drop_states_sql_st(p)
#c.load_states_sql_st(p)
#c.drop_states_sql_st(p)
gnafP = 'AUG19_GNAF_PipeSeparatedValue/G-NAF_AUGUST_2019/'
ds = Process.Do_Stuff('spatialite_db')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_CHANGE_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.FLAT_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.GEOCODED_LEVEL_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.GEOCODE_RELIABILITY_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.GEOCODE_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.LEVEL_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.LOCALITY_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.MB_MATCH_CODE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.PS_JOIN_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_CLASS_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_SUFFIX_AUT(),gnafP,'Authority_Code/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.STREET_LOCALITY_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/'),'testing')

ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_ALIAS(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_DEFAULT_GEOCODE(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_DETAIL(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_FEATURE(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_MESH_BLOCK_2011(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_MESH_BLOCK_2016(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_SITE(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_SITE_GEOCODE(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY_NEIGHBOUR(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY_POINT(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.MB_2011(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.MB_2016(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.PRIMARY_SECONDARY(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STATE(),gnafP,'Standard/'),'testing')
ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STREET_LOCALITY(),gnafP,'Standard/'),'testing')
#ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STREET_LOCALITY_ALIAS(),gnafP,'Standard/'),'testing')
#ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.STREET_LOCALITY_POINT(),gnafP,'Standard/'),'testing')
#ds.sql_to_db(Process.Collate.create_merge_standard_sql_st(Tables.Standard.LOCALITY_ALIAS(),gnafP,'Standard/'),'testing')


#ADDRESS_ALIAS
#ADDRESS_DEFAULT_GEOCODE
#ADDRESS_DETAIL
#ADDRESS_FEATURE
#- ADDRESS_MESH_BLOCK_2011
#- ADDRESS_MESH_BLOCK_2016
#- ADDRESS_SITE
#- ADDRESS_SITE_GEOCODE
#- LOCALITY
#- LOCALITY_NEIGHBOUR
#- LOCALITY_POINT
#- MB_2011
#- MB_2016
#- PRIMARY_SECONDARY
#- STATE
#- STREET_LOCALITY
#- STREET_LOCALITY_ALIAS
#- STREET_LOCALITY_POINT
#- LOCALITY_ALIAS















#Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/')



#Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_CHANGE_TYPE_AUT(),gnafP,'Authority_Code/')

#http://grainier.net/iterate-and-initialize-all-sub-classes-in-python/

