class Defaults:
    """
    """
    

    __slots__ = ("gnaf_path","states9","states8","sqlLoad")
    
    def __init__(self):
        self.gnaf_path = ''
        self.states9 = ['NSW','VIC','QLD','SA','WA','TAS','NT','ACT','OT']
        self.states8 = ['NSW','VIC','QLD','SA','WA','TAS','NT','ACT']
        self.sqlLoad = """.mode csv {table}
.import {filespath}{subdir}{table}.csv {table}"""
        
        
        
class Tables:
    
    class Standard:
        
    
        class ADDRESS_ALIAS:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_ALIAS_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_ALIAS_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_ALIAS_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_ALIAS";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_ALIAS_SRC" AS'
                self.sqlState = """SELECT address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment
FROM {state}_ADDRESS_ALIAS_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_ALIAS (
 address_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 principal_pid varchar(15) NOT NULL,
 alias_pid varchar(15) NOT NULL,
 alias_type_code varchar(10) NOT NULL,
 alias_comment varchar(200)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_ALIAS SELECT
 address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment
FROM ADDRESS_ALIAS_SRC;"""
                
        class ADDRESS_DEFAULT_GEOCODE:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_DEFAULT_GEOCODE_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_DEFAULT_GEOCODE_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_DEFAULT_GEOCODE_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_DEFAULT_GEOCODE";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_DEFAULT_GEOCODE_SRC" AS'
                self.sqlState = """SELECT address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM {state}_ADDRESS_DEFAULT_GEOCODE_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_DEFAULT_GEOCODE (
 address_default_geocode_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 geocode_type_code varchar(4) NOT NULL,
 longitude numeric(11,8),
 latitude numeric(10,8)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_DEFAULT_GEOCODE
SELECT address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM ADDRESS_DEFAULT_GEOCODE_SRC;"""

        class ADDRESS_DETAIL:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_DETAIL_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_DETAIL_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_DETAIL_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_DETAIL";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_DETAIL_SRC" AS'
                self.sqlState = """SELECT address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM {state}_ADDRESS_DETAIL_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_DETAIL (
 address_detail_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_last_modified date,
 date_retired date,
 building_name varchar(200),
 lot_number_prefix varchar(2),
 lot_number varchar(5),
 lot_number_suffix varchar(2),
 flat_type_code varchar(7),
 flat_number_prefix varchar(2),
 flat_number numeric(5),
 flat_number_suffix varchar(2),
 level_type_code varchar(4),
 level_number_prefix varchar(2),
 level_number numeric(3),
 level_number_suffix varchar(2),
 number_first_prefix varchar(3),
 number_first numeric(6),
 number_first_suffix varchar(2),
 number_last_prefix varchar(3),
 number_last numeric(6),
 number_last_suffix varchar(2),
 street_locality_pid varchar(15),
 location_description varchar(45),
 locality_pid varchar(15) NOT NULL,
 alias_principal char(1),
 postcode varchar(4),
 private_street varchar(75),
 legal_parcel_id varchar(20),
 confidence numeric(1),
 address_site_pid varchar(15) NOT NULL,
 level_geocoded_code numeric(2) NOT NULL,
 property_pid varchar(15),
 gnaf_property_pid varchar(15),
 primary_secondary varchar(1)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_DETAIL
SELECT address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM ADDRESS_DETAIL_SRC;"""


        class ADDRESS_FEATURE:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states8
                self.filePiped = '{state}_ADDRESS_FEATURE_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_FEATURE_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_FEATURE_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_FEATURE";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_FEATURE_SRC" AS'
                self.sqlState = """SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code
FROM {state}_ADDRESS_FEATURE_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_FEATURE (
 address_feature_id varchar(16) NOT NULL,
 address_feature_pid varchar(16) NOT NULL,
 address_detail_pid varchar(15) NOT NULL,
 date_address_detail_created date NOT NULL,
 date_address_detail_retired date,
 address_change_type_code varchar(50)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_FEATURE
SELECT address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM ADDRESS_FEATURE_SRC;"""
        
        class ADDRESS_MESH_BLOCK_2011:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_MESH_BLOCK_2011_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_MESH_BLOCK_2011_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_MESH_BLOCK_2011_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_MESH_BLOCK_2011";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_MESH_BLOCK_2011_SRC" AS'
                self.sqlState = """SELECT  address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM {state}_ADDRESS_MESH_BLOCK_2011_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_MESH_BLOCK_2011 (
 address_mesh_block_2011_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 mb_match_code varchar(15) NOT NULL,
 mb_2011_pid varchar(15) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_MESH_BLOCK_2011
SELECT address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM  ADDRESS_MESH_BLOCK_2011_SRC;"""

        class ADDRESS_MESH_BLOCK_2016:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_MESH_BLOCK_2016_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_MESH_BLOCK_2016_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_MESH_BLOCK_2016_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_MESH_BLOCK_2016";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_MESH_BLOCK_2016_SRC" AS'
                self.sqlState = """SELECT address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM {state}_ADDRESS_MESH_BLOCK_2016_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_MESH_BLOCK_2016 (
 address_mesh_block_2016_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 mb_match_code varchar(15) NOT NULL,
 mb_2016_pid varchar(15) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_MESH_BLOCK_2016
SELECT address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM ADDRESS_MESH_BLOCK_2016_SRC;"""

        class ADDRESS_SITE:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_SITE_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_SITE_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_SITE_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_SITE";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_SITE_SRC" AS'
                self.sqlState = """SELECT address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM {state}_ADDRESS_SITE_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_SITE (
 address_site_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_type varchar(8),
 address_site_name varchar(200)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_SITE
SELECT address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM ADDRESS_SITE_SRC;"""

        class ADDRESS_SITE_GEOCODE:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_ADDRESS_SITE_GEOCODE_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_ADDRESS_SITE_GEOCODE_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "ADDRESS_SITE_GEOCODE_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "ADDRESS_SITE_GEOCODE";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_SITE_GEOCODE_SRC" AS'
                self.sqlState = """SELECT address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM {state}_ADDRESS_SITE_GEOCODE_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_SITE_GEOCODE (
 address_site_geocode_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_site_pid varchar(15),
 geocode_site_name varchar(200),
 geocode_site_description varchar(45),
 geocode_type_code varchar(4),
 reliability_code numeric(1) NOT NULL,
 boundary_extent numeric(7),
 planimetric_accuracy numeric(12),
 elevation numeric(7),
 longitude numeric(11,8),
 latitude numeric(10,8)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_SITE_GEOCODE
SELECT address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM ADDRESS_SITE_GEOCODE_SRC;"""

        class LOCALITY:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_LOCALITY_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_LOCALITY_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "LOCALITY_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "LOCALITY";'
                self.sqlStart = 'CREATE TABLE "LOCALITY_SRC" AS'
                self.sqlState = """SELECT locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM {state}_LOCALITY_psv"""
                self.sqlTable = """CREATE TABLE LOCALITY (
 locality_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_name varchar(100) NOT NULL,
 primary_postcode varchar(4),
 locality_class_code char(1) NOT NULL,
 state_pid varchar(15) NOT NULL,
 gnaf_locality_pid varchar(15),
 gnaf_reliability_code numeric(1) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO LOCALITY
SELECT locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM LOCALITY_SRC;"""
                

        class LOCALITY_NEIGHBOUR:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_LOCALITY_NEIGHBOUR_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_LOCALITY_NEIGHBOUR_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "LOCALITY_NEIGHBOUR_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "LOCALITY_NEIGHBOUR";'
                self.sqlStart = 'CREATE TABLE "LOCALITY_NEIGHBOUR_SRC" AS'
                self.sqlState = """SELECT  locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM {state}_LOCALITY_NEIGHBOUR_psv"""
                self.sqlTable = """CREATE TABLE LOCALITY_NEIGHBOUR (
 locality_neighbour_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 neighbour_locality_pid varchar(15) NOT NULL
);
"""
                self.sqlInsert = """INSERT INTO LOCALITY_NEIGHBOUR
SELECT locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM LOCALITY_NEIGHBOUR_SRC;"""

        class LOCALITY_POINT:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_LOCALITY_POINT_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_LOCALITY_POINT_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "LOCALITY_POINT_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "LOCALITY_POINT";'
                self.sqlStart = 'CREATE TABLE "LOCALITY_POINT_SRC" AS'
                self.sqlState = """SELECT locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM {state}_LOCALITY_POINT_psv"""
                self.sqlTable = """CREATE TABLE LOCALITY_POINT (
 locality_point_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 planimetric_accuracy numeric(12),
 longitude numeric(11,8),
 latitude numeric(10,8)
);"""
                self.sqlInsert = """INSERT INTO LOCALITY_POINT
SELECT locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM LOCALITY_POINT_SRC;"""


        class MB_2011:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_MB_2011_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_MB_2011_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "MB_2011_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "MB_2011";'
                self.sqlStart = 'CREATE TABLE "MB_2011_SRC" AS'
                self.sqlState = """SELECT mb_2011_pid,date_created,date_retired,mb_2011_code
FROM {state}_MB_2011_psv"""
                self.sqlTable = """CREATE TABLE "MB_2011" (
 mb_2011_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 mb_2011_code varchar(15) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO "MB_2011"
SELECT mb_2011_pid,date_created,date_retired,mb_2011_code
FROM MB_2011_SRC;"""

        class MB_2016:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_MB_2016_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_MB_2016_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "MB_2016_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "MB_2016";'
                self.sqlStart = 'CREATE TABLE "MB_2016_SRC" AS'
                self.sqlState = """SELECT mb_2016_pid,date_created,date_retired,mb_2016_code
FROM {state}_MB_2016_psv"""
                self.sqlTable = """CREATE TABLE "MB_2016" (
 mb_2016_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 mb_2016_code varchar(15) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO "MB_2016"
SELECT mb_2016_pid,date_created,date_retired,mb_2016_code
FROM MB_2016_SRC;"""

        class PRIMARY_SECONDARY:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_PRIMARY_SECONDARY_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_PRIMARY_SECONDARY_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "PRIMARY_SECONDARY_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "PRIMARY_SECONDARY";'
                self.sqlStart = 'CREATE TABLE "PRIMARY_SECONDARY_SRC" AS'
                self.sqlState = """SELECT  primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM {state}_PRIMARY_SECONDARY_psv"""
                self.sqlTable = """CREATE TABLE PRIMARY_SECONDARY (
 primary_secondary_pid varchar(15) NOT NULL,
 primary_pid varchar(15) NOT NULL,
 secondary_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 ps_join_type_code numeric(2) NOT NULL,
 ps_join_comment varchar(500)
);"""
                self.sqlInsert = """INSERT INTO PRIMARY_SECONDARY
SELECT primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM PRIMARY_SECONDARY_SRC;"""


        class STATE:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_STATE_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_STATE_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "STATE_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "STATE";'
                self.sqlStart = 'CREATE TABLE "STATE_SRC" AS'
                self.sqlState = """SELECT  state_pid,date_created,date_retired,state_name,state_abbreviation
FROM {state}_STATE_psv"""
                self.sqlTable = """CREATE TABLE STATE (
 state_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 state_name varchar(50) NOT NULL,
 state_abbreviation varchar(3) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO STATE
SELECT state_pid,date_created,date_retired,state_name,state_abbreviation
FROM STATE_SRC;"""


        class STREET_LOCALITY:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_STREET_LOCALITY_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_STREET_LOCALITY_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "STREET_LOCALITY_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "STREET_LOCALITY";'
                self.sqlStart = 'CREATE TABLE "STREET_LOCALITY_SRC" AS'
                self.sqlState = """SELECT street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM {state}_STREET_LOCALITY_psv"""
                self.sqlTable = """CREATE TABLE STREET_LOCALITY (
 street_locality_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 street_class_code char(1) NOT NULL,
 street_name varchar(100) NOT NULL,
 street_type_code varchar(15),
 street_suffix_code varchar(15),
 locality_pid varchar(15) NOT NULL,
 gnaf_street_pid varchar(15),
 gnaf_street_confidence numeric(1),
 gnaf_reliability_code numeric(1) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO STREET_LOCALITY  SELECT
 street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
 STREET_LOCALITY_SRC;"""

        class STREET_LOCALITY_ALIAS:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_STREET_LOCALITY_ALIAS_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_STREET_LOCALITY_ALIAS_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "STREET_LOCALITY_ALIAS_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "STREET_LOCALITY_ALIAS";'
                self.sqlStart = 'CREATE TABLE "STREET_LOCALITY_ALIAS_SRC" AS'
                self.sqlState = """SELECT street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM {state}_STREET_LOCALITY_ALIAS_psv"""
                self.sqlTable = """CREATE TABLE STREET_LOCALITY_ALIAS (
 street_locality_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 street_locality_pid varchar(15) NOT NULL,
 street_name varchar(100) NOT NULL,
 street_type_code varchar(15),
 street_suffix_code varchar(15),
 alias_type_code varchar(10) NOT NULL
);
"""
                self.sqlInsert = """INSERT INTO STREET_LOCALITY_ALIAS
SELECT  street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM STREET_LOCALITY_ALIAS_SRC;"""


        class STREET_LOCALITY_POINT:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_STREET_LOCALITY_POINT_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_STREET_LOCALITY_POINT_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "STREET_LOCALITY_POINT_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "STREET_LOCALITY_POINT";'
                self.sqlStart = 'CREATE TABLE "STREET_LOCALITY_POINT_SRC" AS'
                self.sqlState = """SELECT  street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM {state}_STREET_LOCALITY_POINT_psv"""
                self.sqlTable = """CREATE TABLE STREET_LOCALITY_POINT (
 street_locality_point_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 street_locality_pid varchar(15) NOT NULL,
 boundary_extent numeric(7),
 planimetric_accuracy numeric(12),
 longitude numeric(11,8),
 latitude numeric(10,8)
);"""
                self.sqlInsert = """INSERT INTO STREET_LOCALITY_POINT
SELECT  street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM  STREET_LOCALITY_POINT_SRC;"""


        class LOCALITY_ALIAS:
            __slots__ = ("stateList","filePiped","sqlDropMrgTbl","sqlDropInpTbl","sqlDropOutTbl","sqlDropInport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                Def = Defaults()
                self.stateList = Def.states9
                self.filePiped = '{state}_LOCALITY_ALIAS_psv'
                self.sqlDropInpTbl = 'DROP TABLE IF EXISTS "{state}_LOCALITY_ALIAS_psv";'
                self.sqlDropMrgTbl = 'DROP TABLE IF EXISTS "LOCALITY_ALIAS_SRC";'
                self.sqlDropOutTbl = 'DROP TABLE IF EXISTS "LOCALITY_ALIAS";'
                self.sqlStart = 'CREATE TABLE "LOCALITY_ALIAS_SRC" AS'
                self.sqlState = """SELECT locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM {state}_LOCALITY_ALIAS_psv"""
                self.sqlTable = """CREATE TABLE LOCALITY_ALIAS (
 locality_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 name varchar(100) NOT NULL,
 postcode varchar(4),
 alias_type_code varchar(10) NOT NULL,
 state_pid varchar(15) NOT NULL
);"""
                self.sqlInsert = """INSERT INTO LOCALITY_ALIAS
SELECT locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM LOCALITY_ALIAS_SRC;"""



    class Authority_Code:
            
        class ADDRESS_ALIAS_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
        
            def __init__(self):
                self.filePiped = 'Authority_Code_ADDRESS_ALIAS_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "ADDRESS_ALIAS_TYPE_AUT";'
                self.sqlTable = """
CREATE TABLE ADDRESS_ALIAS_TYPE_AUT (
 code varchar(10) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(30)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_ALIAS_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_ADDRESS_ALIAS_TYPE_AUT_psv;
"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_ADDRESS_ALIAS_TYPE_AUT_psv";'
                
        class ADDRESS_CHANGE_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_ADDRESS_CHANGE_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "ADDRESS_CHANGE_TYPE_AUT";'
                self.sqlTable = """
CREATE TABLE ADDRESS_CHANGE_TYPE_AUT (
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);"""
                self.sqlInsert = """
INSERT INTO ADDRESS_CHANGE_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_ADDRESS_CHANGE_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_ADDRESS_CHANGE_TYPE_AUT_psv";'

        class ADDRESS_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_ADDRESS_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "ADDRESS_TYPE_AUT";'
                self.sqlTable = """CREATE TABLE ADDRESS_TYPE_AUT (
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_ADDRESS_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_ADDRESS_TYPE_AUT_psv";'

        class FLAT_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_FLAT_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "FLAT_TYPE_AUT";'
                self.sqlTable = """CREATE TABLE FLAT_TYPE_AUT (
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);"""
                self.sqlInsert = """INSERT INTO FLAT_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_FLAT_TYPE_AUT_psv;"""

                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_FLAT_TYPE_AUT_psv";'
                
                
        class GEOCODED_LEVEL_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_GEOCODED_LEVEL_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "GEOCODED_LEVEL_TYPE_AUT";'
                self.sqlTable = """CREATE TABLE GEOCODED_LEVEL_TYPE_AUT (
 code numeric(2) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(70)
);"""
                self.sqlInsert = """INSERT INTO GEOCODED_LEVEL_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_GEOCODED_LEVEL_TYPE_AUT_psv;"""

                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_GEOCODED_LEVEL_TYPE_AUT_psv";'


        class GEOCODE_RELIABILITY_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_GEOCODE_RELIABILITY_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "GEOCODE_RELIABILITY_AUT";'
                self.sqlTable = """
CREATE TABLE GEOCODE_RELIABILITY_AUT (
 code numeric(1) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(100)
);"""
                self.sqlInsert = """
INSERT INTO GEOCODE_RELIABILITY_AUT
SELECT code,name,description
FROM Authority_Code_GEOCODE_RELIABILITY_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_GEOCODE_RELIABILITY_AUT_psv";'
                
        class GEOCODE_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_GEOCODE_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "GEOCODE_TYPE_AUT";'
                self.sqlTable = """
CREATE TABLE GEOCODE_TYPE_AUT (
 code numeric(4) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(250)
);"""
                self.sqlInsert = """
INSERT INTO GEOCODE_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_GEOCODE_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_GEOCODE_TYPE_AUT_psv";'
                
        class LEVEL_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_LEVEL_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "LEVEL_TYPE_AUT";'
                self.sqlTable = """CREATE TABLE LEVEL_TYPE_AUT (
 code varchar(4) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(30)
);"""
                self.sqlInsert = """INSERT INTO LEVEL_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_LEVEL_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_LEVEL_TYPE_AUT_psv";'
                
        class LOCALITY_ALIAS_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_LOCALITY_ALIAS_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "LOCALITY_ALIAS_TYPE_AUT";'
                self.sqlTable = """
CREATE TABLE LOCALITY_ALIAS_TYPE_AUT (
 code varchar(10) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(100)
);"""
                self.sqlInsert = """
INSERT INTO LOCALITY_ALIAS_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_LOCALITY_ALIAS_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_LOCALITY_ALIAS_TYPE_AUT_psv";'
                
        class LOCALITY_CLASS_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_LOCALITY_CLASS_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "LOCALITY_CLASS_AUT";'
                self.sqlTable = """
CREATE TABLE LOCALITY_CLASS_AUT (
 code char(1) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(200)
);"""
                self.sqlInsert = """
INSERT INTO LOCALITY_CLASS_AUT
SELECT code,name,description
FROM Authority_Code_LOCALITY_CLASS_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_LOCALITY_CLASS_AUT_psv";'
                
        class MB_MATCH_CODE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_MB_MATCH_CODE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "MB_MATCH_CODE_AUT";'
                self.sqlTable = """
CREATE TABLE MB_MATCH_CODE_AUT (
 code varchar(15) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(250)
);"""
                self.sqlInsert = """
INSERT INTO MB_MATCH_CODE_AUT
SELECT code,name,description
FROM Authority_Code_MB_MATCH_CODE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_MB_MATCH_CODE_AUT_psv";'
                
        class PS_JOIN_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_PS_JOIN_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "PS_JOIN_TYPE_AUT";'
                self.sqlTable = """
CREATE TABLE PS_JOIN_TYPE_AUT (
 code numeric(2) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(500)
);"""
                self.sqlInsert = """
INSERT INTO PS_JOIN_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_PS_JOIN_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_PS_JOIN_TYPE_AUT_psv";'

        class STREET_CLASS_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_STREET_CLASS_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "STREET_CLASS_AUT";'
                self.sqlTable = """
CREATE TABLE STREET_CLASS_AUT (
 code char(1) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(200)
);"""
                self.sqlInsert = """
INSERT INTO STREET_CLASS_AUT
SELECT code,name,description
FROM Authority_Code_STREET_CLASS_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_STREET_CLASS_AUT_psv";'

        class STREET_SUFFIX_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_STREET_SUFFIX_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "STREET_SUFFIX_AUT";'
                self.sqlTable = """
CREATE TABLE STREET_SUFFIX_AUT (
 code varchar(15) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(30)
);"""
                self.sqlInsert = """
INSERT INTO STREET_SUFFIX_AUT
SELECT code,name,description
FROM Authority_Code_STREET_SUFFIX_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_STREET_SUFFIX_AUT_psv";'

        class STREET_LOCALITY_ALIAS_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_STREET_LOCALITY_ALIAS_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "STREET_LOCALITY_ALIAS_TYPE_AUT";'
                self.sqlTable = """
CREATE TABLE STREET_LOCALITY_ALIAS_TYPE_AUT (
 code varchar(10) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(15)
);"""
                self.sqlInsert = """
INSERT INTO STREET_LOCALITY_ALIAS_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_STREET_LOCALITY_ALIAS_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_STREET_LOCALITY_ALIAS_TYPE_AUT_psv";'
