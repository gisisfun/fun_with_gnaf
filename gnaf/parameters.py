class Defaults:
    """
    """
    

    __slots__ = ("sqlitePath","gnaf_path","states9","states8","sqlLoad")
    
    def __init__(self):
        self.sqlitePath = 'spatialite_db'
        self.gnaf_path = ''
        self.states9 = ['NSW','VIC','QLD','SA','WA','TAS','NT','ACT','OT']
        self.states8 = ['NSW','VIC','QLD','SA','WA','TAS','NT','ACT']
        self.sqlLoad = """.mode csv {table}
.import {filespath}{subdir}{table}.csv {table}"""
       
class OSVars:
    """
    Operating System Dependant values for 'posix' and 'nt'
    """

    class posix:
        __slots__ = ("Slash","Ogr2ogr","Spatialite")
        def __init__(self):
            self.Slash = '/'
            self.Sqlite3 = '/usr/bin/sqlite3'
        
    class nt:
        __slots__ = ("Slash","Ogr2ogr","Spatialite")
        def __init__(self):
            self.Slash = '\\'
            self.Sqlite3 = 'c:\\OSGeo4W64\\bin\\sqlite3.exe'
        
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
 address_alias_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 principal_pid varchar(15) NOT NULL,
 alias_pid varchar(15) NOT NULL,
 alias_type_code varchar(10) NOT NULL,
 alias_comment varchar(200),
 FOREIGN KEY (alias_type_code)
  REFERENCES ADDRESS_ALIAS_TYPE_AUT (code),
 FOREIGN KEY (alias_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid),
 FOREIGN KEY (principal_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid)
 
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
 address_default_geocode_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 geocode_type_code varchar(4) NOT NULL,
 longitude numeric(11,8),
 latitude numeric(10,8),
 FOREIGN KEY (address_detail_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid),
 FOREIGN KEY (geocode_type_code)
  REFERENCES GEOCODE_TYPE_AUT (code)
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
                self.sqlState = """SELECT address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, printf('%04d', postcode) AS postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM {state}_ADDRESS_DETAIL_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_DETAIL (
 address_detail_pid varchar(15) NOT NULL PRIMARY KEY,
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
 primary_secondary varchar(1),
 FOREIGN KEY (address_site_pid)
  REFERENCES ADDRESS_SITE (address_site_pid),
 FOREIGN KEY (flat_type_code)
  REFERENCES FLAT_TYPE_AUT (code),
 FOREIGN KEY (level_geocoded_code)
  REFERENCES GEOCODED_LEVEL_TYPE_AUT (code),
 FOREIGN KEY (level_type_code)
  REFERENCES LEVEL_TYPE_AUT (code),
 FOREIGN KEY (locality_pid)
  REFERENCES LOCALITY (locality_pid),
 FOREIGN KEY (locality_pid)
  REFERENCES LOCALITY_ALIAS (locality_alias_pid),
 FOREIGN KEY (street_locality_pid)
  REFERENCES STREET_LOCALITY (street_locality_pid),
 FOREIGN KEY (street_locality_pid)
  REFERENCES STREET_LOCALITY_ALIAS (street_locality_alias_pid),
 FOREIGN KEY (street_locality_pid)
  REFERENCES STREET_LOCALITY_NEIGHBOUR (street_locality_neighbour_pid)  
 
);"""
                self.sqlInsert = """INSERT INTO ADDRESS_DETAIL
SELECT address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, printf('%04d', postcode) AS postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
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
 address_feature_id varchar(16) NOT NULL PRIMARY KEY,
 address_feature_pid varchar(16) NOT NULL,
 address_detail_pid varchar(15) NOT NULL,
 date_address_detail_created date NOT NULL,
 date_address_detail_retired date,
 address_change_type_code varchar(50),
 FOREIGN KEY (address_change_type_code)
  REFERENCES ADDRESS_CHANGE_TYPE_AUT (code),
 FOREIGN KEY (address_detail_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid)
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
 address_mesh_block_2011_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 mb_match_code varchar(15) NOT NULL,
 mb_2011_pid varchar(15) NOT NULL,
 FOREIGN KEY (address_detail_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid),
 FOREIGN KEY (mb_2011_pid)
  REFERENCES MB_2011 (mb_2011_pid),
 FOREIGN KEY (mb_match_code)
  REFERENCES MB_MATCH_CODE_AUT (code)
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
 address_mesh_block_2016_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 mb_match_code varchar(15) NOT NULL,
 mb_2016_pid varchar(15) NOT NULL,
 FOREIGN KEY (address_detail_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid),
 FOREIGN KEY (mb_2016_pid)
  REFERENCES MB_2016 (mb_2016_pid),
 FOREIGN KEY (mb_match_code)
  REFERENCES MB_MATCH_CODE_AUT (code)
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
 address_site_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 address_type varchar(8),
 address_site_name varchar(200),
 FOREIGN KEY (address_type)
  REFERENCES ADDRESS_TYPE_AUT (code)
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
 address_site_geocode_pid varchar(15) NOT NULL PRIMARY KEY,
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
 latitude numeric(10,8),
 FOREIGN KEY (address_site_pid)
  REFERENCES ADDRESS_SITE (address_site_pid),
 FOREIGN KEY (geocode_type_code)
  REFERENCES GEOCODE_TYPE_AUT (code),
 FOREIGN KEY (reliability_code)
  REFERENCES GEOCODE_RELIABILITY_AUT (code)
 
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
 locality_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 locality_name varchar(100) NOT NULL,
 primary_postcode varchar(4),
 locality_class_code char(1) NOT NULL,
 state_pid varchar(15) NOT NULL,
 gnaf_locality_pid varchar(15),
 gnaf_reliability_code numeric(1) NOT NULL,
 FOREIGN KEY (gnaf_reliability_code)
  REFERENCES GEOCODE_RELIABILITY_AUT (code)
 
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
 locality_neighbour_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 neighbour_locality_pid varchar(15) NOT NULL,
 FOREIGN KEY (locality_pid)
  REFERENCES LOCALITY (locality_pid),
 FOREIGN KEY (neighbour_locality_pid)
  REFERENCES LOCALITY (locality_pid)
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
 locality_point_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 planimetric_accuracy numeric(12),
 longitude numeric(11,8),
 latitude numeric(10,8),
 FOREIGN KEY (locality_pid)
  REFERENCES LOCALITY (locality_pid)
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
 mb_2011_pid varchar(15) NOT NULL PRIMARY KEY,
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
 mb_2016_pid varchar(15) NOT NULL PRIMARY KEY,
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
 primary_secondary_pid varchar(15) NOT NULL PRIMARY KEY,
 primary_pid varchar(15) NOT NULL,
 secondary_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 ps_join_type_code numeric(2) NOT NULL,
 ps_join_comment varchar(500),
 FOREIGN KEY (primary_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid),
 FOREIGN KEY (ps_join_type_code)
  REFERENCES PS_JOIN_TYPE_AUT (code),
 FOREIGN KEY (secondary_pid)
  REFERENCES ADDRESS_DETAIL (address_detail_pid)
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
 state_pid varchar(15) NOT NULL PRIMARY KEY,
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
 street_locality_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 street_class_code char(1) NOT NULL,
 street_name varchar(100) NOT NULL,
 street_type_code varchar(15),
 street_suffix_code varchar(15),
 locality_pid varchar(15) NOT NULL,
 gnaf_street_pid varchar(15),
 gnaf_street_confidence numeric(1),
 gnaf_reliability_code numeric(1) NOT NULL,
 FOREIGN KEY (gnaf_reliability_code)
  REFERENCES GEOCODE_RELIABILITY_AUT (code),
 FOREIGN KEY (locality_pid)
  REFERENCES LOCALITY (locality_pid),
 FOREIGN KEY (street_class_code)
  REFERENCES STREET_CLASS_AUT (code),
 FOREIGN KEY (street_suffix_code)
  REFERENCES STREET_SUFFIX_AUT (code),
 FOREIGN KEY (street_type_code)
  REFERENCES STREET_TYPE_AUT (code)
 
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
 street_locality_alias_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 street_locality_pid varchar(15) NOT NULL,
 street_name varchar(100) NOT NULL,
 street_type_code varchar(15),
 street_suffix_code varchar(15),
 alias_type_code varchar(10) NOT NULL,
 FOREIGN KEY (alias_type_code)
  REFERENCES STREET_LOCALITY_ALIAS_TYPE_AUT (code),
 FOREIGN KEY (street_locality_pid)
  REFERENCES STREET_LOCALITY (street_locality_pid),
 FOREIGN KEY (street_suffix_code)
  REFERENCES STREET_SUFFIX_AUT (code),
 FOREIGN KEY (street_type_code)
  REFERENCES STREET_TYPE_AUT (code)
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
 street_locality_point_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 street_locality_pid varchar(15) NOT NULL,
 boundary_extent numeric(7),
 planimetric_accuracy numeric(12),
 longitude numeric(11,8),
 latitude numeric(10,8),
 FOREIGN KEY (street_locality_pid)
  REFERENCES STREET_LOCALITY (street_locality_pid),
  FOREIGN KEY (street_locality_pid)
  REFERENCES STREET_LOCALITY_ALIAS (street_locality_alias_pid)
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
                self.sqlState = """SELECT locality_alias_pid,date_created,date_retired,locality_pid,name,printf('%04d', postcode) AS postcode,alias_type_code,state_pid
FROM {state}_LOCALITY_ALIAS_psv"""
                self.sqlTable = """CREATE TABLE LOCALITY_ALIAS (
 locality_alias_pid varchar(15) NOT NULL PRIMARY KEY,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 name varchar(100) NOT NULL,
 postcode varchar(4),
 alias_type_code varchar(10) NOT NULL,
 state_pid varchar(15) NOT NULL,
 FOREIGN KEY (alias_type_code)
  REFERENCES LOCALITY_ALIAS_TYPE_AUT (code),
 FOREIGN KEY (locality_pid)
  REFERENCES LOCALITY (locality_pid)
 
);"""
                self.sqlInsert = """INSERT INTO LOCALITY_ALIAS
SELECT locality_alias_pid,date_created,date_retired,locality_pid,name, printf('%04d', postcode) AS postcode,alias_type_code,state_pid
FROM LOCALITY_ALIAS_SRC;"""



    class Authority_Code:
            
        class ADDRESS_ALIAS_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
        
            def __init__(self):
                self.filePiped = 'Authority_Code_ADDRESS_ALIAS_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "ADDRESS_ALIAS_TYPE_AUT";'
                self.sqlTable = """CREATE TABLE ADDRESS_ALIAS_TYPE_AUT (
 code varchar(10) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE ADDRESS_CHANGE_TYPE_AUT (
 code varchar(50) NOT NULL PRIMARY KEY,
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
 code varchar(50) NOT NULL PRIMARY KEY,
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
 code varchar(50) NOT NULL PRIMARY KEY,
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
 code numeric(2) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE GEOCODE_RELIABILITY_AUT (
 code numeric(1) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE GEOCODE_TYPE_AUT (
 code numeric(4) NOT NULL PRIMARY KEY,
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
 code varchar(4) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE LOCALITY_ALIAS_TYPE_AUT (
 code varchar(10) NOT NULL PRIMARY KEY,
 name varchar(50) NOT NULL,
 description varchar(100)
);"""
                self.sqlInsert = """INSERT INTO LOCALITY_ALIAS_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_LOCALITY_ALIAS_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_LOCALITY_ALIAS_TYPE_AUT_psv";'
                
        class LOCALITY_CLASS_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_LOCALITY_CLASS_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "LOCALITY_CLASS_AUT";'
                self.sqlTable = """CREATE TABLE LOCALITY_CLASS_AUT (
 code char(1) NOT NULL PRIMARY KEY,
 name varchar(50) NOT NULL,
 description varchar(200)
);"""
                self.sqlInsert = """INSERT INTO LOCALITY_CLASS_AUT
SELECT code,name,description
FROM Authority_Code_LOCALITY_CLASS_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_LOCALITY_CLASS_AUT_psv";'
                
        class MB_MATCH_CODE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_MB_MATCH_CODE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "MB_MATCH_CODE_AUT";'
                self.sqlTable = """CREATE TABLE MB_MATCH_CODE_AUT (
 code varchar(15) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE PS_JOIN_TYPE_AUT (
 code numeric(2) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE STREET_CLASS_AUT (
 code char(1) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE STREET_SUFFIX_AUT (
 code varchar(15) NOT NULL PRIMARY KEY,
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
                self.sqlTable = """CREATE TABLE STREET_LOCALITY_ALIAS_TYPE_AUT (
 code varchar(10) NOT NULL PRIMARY KEY,
 name varchar(50) NOT NULL,
 description varchar(15)
);"""
                self.sqlInsert = """
INSERT INTO STREET_LOCALITY_ALIAS_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_STREET_LOCALITY_ALIAS_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_STREET_LOCALITY_ALIAS_TYPE_AUT_psv";'

        class STREET_TYPE_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_STREET_TYPE_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "STREET_TYPE_AUT";'
                self.sqlTable = """CREATE TABLE STREET_TYPE_AUT (
 code varchar(15) NOT NULL PRIMARY KEY,
 name varchar(50) NOT NULL,
 description varchar(15)
);"""
                self.sqlInsert = """INSERT INTO STREET_TYPE_AUT
SELECT code,name,description
FROM Authority_Code_STREET_TYPE_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_STREET_TYPE_AUT_psv";'

        class STREET_SUFFIX_AUT:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlTable","sqlInsert","sqlDropInpTbl")
    
            def __init__(self):
                self.filePiped = 'Authority_Code_STREET_SUFFIX_AUT_psv'
                self.sqlDropOutTbl = 'DROP TABLE if exists "STREET_SUFFIX_AUT";'
                self.sqlTable = """CREATE TABLE STREET_SUFFIX_AUT (
 code varchar(15) NOT NULL PRIMARY KEY,
 name varchar(50) NOT NULL,
 description varchar(15)
);"""
                self.sqlInsert = """INSERT INTO STREET_SUFFIX_AUT
SELECT code,name,description
FROM Authority_Code_STREET_SUFFIX_AUT_psv;"""
                self.sqlDropInpTbl = 'DROP TABLE if exists "Authority_Code_STREET_SUFFIX_AUT_psv";'



    class Views:
        class ADDRESS_VIEW:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlView")
            
            def __init__(self):
                self.filePiped = 'ADDRESS_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "ADDRESS_VIEW";'
                self.sqlView = """CREATE VIEW ADDRESS_VIEW AS
SELECT AD.address_detail_pid as Address_Detail_PID,
AD.street_locality_pid as Street_Locality_PID,
AD.locality_pid as Locality_PID,
AD.building_name as Building_Name,
AD.lot_number_prefix as Lot_Number_Prefix,
AD.lot_number as Lot_Number,
AD.lot_number_suffix as Lot_Number_Suffix,
FTA.name as Flat_Type,
AD.flat_number_prefix as Flat_Number_Prefix,
AD.flat_number as Flat_Number,
AD.flat_number_suffix as Flat_Number_Suffix,
LTA.name as Level_Type,
AD.level_number as Level_Number,
AD.number_first_prefix as Number_First_Prefix,
AD.number_first as Number_First,
SL.street_name as Street_Name,
SL.street_type_code as Street_Type_Code,
L.locality_name as Locality_Name,
ST.state_abbreviation as State_Abbreviation,
AD.postcode as Postcode,
AD.confidence as Confidence,
(Flat_Type_Code || " " || 
 Flat_Number || " " || 
 Building_Name || " " || 
 Number_First || " " || 
 Street_Name || " " || 
 Street_Type_Code || " " || 
 Locality_Name || " " ||
 State_Abbreviation || " " || 
 Postcode  ) as AddressText,
 ADG.latitude as Latitude,
ADG.longitude as Longitude,
GTA.name as Geocode_Type
FROM
[ADDRESS_DETAIL] as AD 
LEFT JOIN [FLAT_TYPE_AUT] as FTA ON AD.flat_type_code=FTA.code
LEFT JOIN [LEVEL_TYPE_AUT] as LTA ON AD.level_type_code=LTA.code
JOIN [STREET_LOCALITY] as SL ON AD.street_locality_pid=SL.street_locality_pid
LEFT JOIN [STREET_SUFFIX_AUT] as SSA ON SL.street_suffix_code=SSA.code
LEFT JOIN [STREET_CLASS_AUT] as SCA ON SL.street_class_code=SCA.code 
LEFT JOIN [STREET_TYPE_AUT] as STA ON SL.STREET_TYPE_CODE=STA.CODE
JOIN [LOCALITY] as L ON AD.locality_pid= L.locality_pid
JOIN [ADDRESS_DEFAULT_GEOCODE] as ADG ON AD.address_detail_pid=ADG.address_detail_pid
LEFT JOIN [GEOCODE_TYPE_AUT] as GTA ON ADG.geocode_type_code=GTA.code
LEFT JOIN [GEOCODED_LEVEL_TYPE_AUT] as GLTA ON AD.level_geocoded_code=GLTA.code
JOIN [STATE] as ST ON L.state_pid=ST.state_pid
WHERE 
AD.confidence > -1
UNION
SELECT AD.address_detail_pid as Address_Detail_PID,
AD.street_locality_pid as Street_Locality_PID,
AD.locality_pid as Locality_PID,
AD.building_name as Building_Name,
AD.lot_number_prefix as Lot_Number_Prefix,
AD.lot_number as Lot_Number,
AD.lot_number_suffix as Lot_Number_Suffix,
FTA.name as Flat_Type,
AD.flat_number_prefix as Flat_Number_Prefix,
AD.flat_number as Flat_Number,
AD.flat_number_suffix as Flat_Number_Suffix,
LTA.name as Level_Type,
AD.level_number as Level_Number,
AD.number_first_prefix as Number_First_Prefix,
AD.number_first as Number_First,
SL.street_name as Street_Name,
SL.street_type_code as Street_Type_Code,
L.name as Locality_Name,
ST.state_abbreviation as State_Abbreviation,
AD.postcode as Postcode,
AD.confidence as Confidence,
(Flat_Type_Code || " " || 
 Flat_Number || " " || 
 Building_Name || " " || 
 Number_First || " " || 
 SL.street_name || " " || 
 SL.street_type_code || " " || 
 L.name || " " ||
 State_Abbreviation || " " || 
 AD.postcode  ) as AddressText,
 ADG.latitude as Latitude,
ADG.longitude as Longitude,
GTA.name as Geocode_Type
FROM
[ADDRESS_DETAIL] as AD 
LEFT JOIN [FLAT_TYPE_AUT] as FTA ON AD.flat_type_code=FTA.code
LEFT JOIN [LEVEL_TYPE_AUT] as LTA ON AD.level_type_code=LTA.code
JOIN [STREET_LOCALITY_ALIAS] as SL ON AD.street_locality_pid=SL.street_locality_pid
LEFT JOIN [STREET_SUFFIX_AUT] as SSA ON SL.street_suffix_code=SSA.code
LEFT JOIN [STREET_TYPE_AUT] as STA ON SL.STREET_TYPE_CODE=STA.CODE
JOIN [LOCALITY_ALIAS] as L ON AD.locality_pid= L.locality_alias_pid
JOIN [ADDRESS_DEFAULT_GEOCODE] as ADG ON AD.address_detail_pid=ADG.address_detail_pid
LEFT JOIN [GEOCODE_TYPE_AUT] as GTA ON ADG.geocode_type_code=GTA.code
LEFT JOIN [GEOCODED_LEVEL_TYPE_AUT] as GLTA ON AD.level_geocoded_code=GLTA.code
JOIN [STATE] as ST ON L.state_pid=ST.state_pid
WHERE 
AD.confidence > -1
"""
        class LOCALITY_VIEW:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlView")
    
            def __init__(self):
                self.filePiped = 'LOCALITY_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "LOCALITY_VIEW";'
                self.sqlView = """CREATE VIEW LOCALITY_VIEW AS
SELECT DISTINCT Loc.locality_name as locality_name,
State.state_abbreviation as state_abbreviation,
AD.postcode as postcode,
Loc_Point.latitude as latitude,
Loc_Point.longitude as longitude
FROM [LOCALITY] as Loc
JOIN [ADDRESS_DETAIL] as AD 
ON Loc.locality_pid = AD.locality_pid
JOIN [LOCALITY_POINT] as Loc_Point
ON Loc.locality_pid = Loc_Point.locality_pid
JOIN [STATE] as State
ON Loc.state_pid = State.state_pid
UNION
SELECT DISTINCT Loc.name as locality_name,
State.state_abbreviation as state_abbreviation,
AD.postcode as postcode,
Loc_Point.latitude as latitude,
Loc_Point.longitude as longitude
FROM [LOCALITY_ALIAS] as Loc
JOIN [ADDRESS_DETAIL] as AD 
ON Loc.locality_alias_pid = AD.locality_pid
JOIN [LOCALITY_POINT] as Loc_Point
ON Loc.locality_alias_pid = Loc_Point.locality_pid
JOIN [STATE] as State
ON Loc.state_pid = State.state_pid;
"""

        class ALIAS_LOCALITY_VIEW:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlView")
    
            def __init__(self):
                self.filePiped = 'ALIAS_LOCALITY_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "ALIAS_LOCALITY_VIEW";'
                self.sqlView = """CREATE VIEW ALIAS_LOCALITY_VIEW AS
SELECT Loc.locality_pid as locality_pid,
Loc.locality_name as locality_name,
Ste.state_abbreviation as state,
Loc.primary_postcode as postcode,
Loc_ALias.locality_alias_pid as alias_locality_pid,
Loc_Alias.name as alias_locality_name
from [LOCALITY_ALIAS] as Loc_Alias 
inner JOIN [LOCALITY] as Loc
ON Loc.locality_pid = Loc_ALias.locality_pid
join [STATE] as Ste
on Loc_Alias.state_pid = Ste.state_pid
where locality_name = 'LYNEHAM'
order by locality_pid

"""

        class SECONDARY_VIEW:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlView")
    
            def __init__(self):
                self.filePiped = 'SECONDARY_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "SECONDARY_VIEW";'
                self.sqlView = """CREATE VIEW SECONDARY_VIEW AS
SELECT PS.primary_secondary_pid as ps_primary_secondary_pid, PS.primary_pid as ps_primary_pid, PS.secondary_pid as ps_secondary_pid,
AD.address_detail_pid as ad_address_detail_pid,
PSJT.name as ps_join_type
FROM [PRIMARY_SECONDARY] AS PS
JOIN [ADDRESS_DETAIL] as AD ON
(PS.secondary_pid = AD.address_detail_pid) and (AD.primary_secondary = 'S')
join [PS_JOIN_TYPE_AUT] as PSJT
ON PS.ps_join_type_code = PSJT.code
"""

        class NEIGHBOUR_LOCALITY_VIEW:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlView")
    
            def __init__(self):
                self.filePiped = 'NEIGHBOUR_LOCALITY_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "NEIGHBOUR_LOCALITY_VIEW";'
                self.sqlView = """CREATE VIEW NEIGHBOUR_LOCALITY_VIEW AS
SELECT Loc.locality_name as locality_name,
Loc_Neighbour.locality_pid as locality_pid,
Loc_Neighbour.locality_neighbour_pid as locality_neighbour_pid,
Loc_Neighbour.neighbour_locality_pid as neighbour_locality_pid

from [LOCALITY_NEIGHBOUR] as Loc_Neighbour 
inner JOIN [LOCALITY] as Loc
ON Loc.locality_pid = Loc_Neighbour.neighbour_locality_pid
order by neighbour_locality_pid
"""

        class NEIGHBOUR_LOCALITY_LIST_VIEW:

            def __init__(self):
                self.filePiped = 'NEIGHBOUR_LOCALITY_LIST_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "NEIGHBOUR_LOCALITY_LIST_VIEW";'
                self.sqlView = """CREATE VIEW NEIGHBOUR_LOCALITY_LIST_VIEW AS
SELECT NLoc.locality_neighbour_pid as locality_neighbour_pid,
NLoc.neighbour_locality_pid as std_neighbour_locality_pid,
NLoc.locality_name as std_locality_name,
NLoc.locality_pid as nbr_locality_pid,
Loc.locality_name as nbr_locality_name
from
[NEIGHBOUR_LOCALITY_VIEW] as NLoc
inner join [LOCALITY] as Loc on
Nloc.locality_pid = Loc.locality_pid
order by std_neighbour_locality_pid
"""
                
        class STREET_LOCALITY_VIEW:
            __slots__ = ("filePiped","sqlDropOutTbl", "sqlView")
    
            def __init__(self):
                self.filePiped = 'STREET_LOCALITY_VIEW'
                self.sqlDropOutTbl = 'DROP VIEW if exists "STREET_LOCALITY_VIEW";'
                self.sqlView = """CREATE VIEW STREET_LOCALITY_VIEW AS
SELECT DISTINCT St_Loc.street_name as street_name,
St_Loc.street_type_code as street_type_code,
Loc.locality_name as locality_name,
State.state_abbreviation as state_abbreviation,
AD.postcode as postcode,
St_Loc_Point.latitude as latitude,
St_Loc_Point.longitude as longitude
from [LOCALITY] as Loc
JOIN [ADDRESS_DETAIL] as AD 
ON Loc.locality_pid = AD.locality_pid
join [STREET_LOCALITY_POINT] as St_Loc_Point
on St_Loc.street_locality_pid = St_Loc_Point.street_locality_pid
join [STREET_LOCALITY] as St_Loc
on St_Loc.locality_pid = Loc.locality_pid
join [STATE] as State
on Loc.state_pid = State.state_pid

UNION

SELECT DISTINCT St_Loc.street_name as street_name,
St_Loc.street_type_code as street_type_code,
Loc.name as locality_name,
State.state_abbreviation as state_abbreviation,
AD.postcode as postcode,
St_Loc_Point.latitude as latitude,
St_Loc_Point.longitude as longitude
from [LOCALITY_ALIAS] as Loc
JOIN [ADDRESS_DETAIL] as AD 
ON Loc.locality_alias_pid = AD.locality_pid
join [STREET_LOCALITY_POINT] as St_Loc_Point
on St_Loc.street_locality_pid = St_Loc_Point.street_locality_pid
join [STREET_LOCALITY_ALIAS] as St_Loc
on St_Loc.Street_locality_pid = Loc.locality_alias_pid
join [STATE] as State
on Loc.state_pid = State.state_pid;
"""
             
class DataSets:
    

    class gnaf_nov_2019_gda2020:
        """
        ABS Australian Boundary
        """  
        ...
        
        class CSVFormat:
            __slots__= ('Description','Format','FilePath','PathToFiles','DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'gnaf_nov_2019_gda2020'
                self.Format = 'CSV'
                self.PathToFiles = 'NOV19_GNAF_PipeSeparatedValue_GDA2020/G-NAF/G-NAF_NOVEMBER_2019/'
                self.FilePath = 'NOV19_GNAF_PipeSeparatedValue_GDA2020{slash}G-NAF{slash}G-NAF_NOVEMBER_2019{slash}Standard{slash}ACT_ADDRESS_ALIAS_psv.psv'
                self.DownURL = 'https://data.gov.au/data/dataset/19432f89-dc3a-4ef3-b943-5326ef1dbecc/resource/fdce090a-b356-4afe-91bb-c78fbf88082a/download/nov19_gnaf_pipeseparatedvalue_gda2020.zip'
                self.ZipDir = 'csv'
                self.ZipPath ='nov19_gnaf_pipeseparatedvalue_gda2020.zip'


    class gnaf_nov_2019:
        """
        ABS Australian Boundary
        """  
        ...
        
        class CSVFormat:
            __slots__= ('Description','Format','FilePath','PathToFiles','DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'gnaf_nov_2019'
                self.Format = 'CSV'
                self.PathToFiles = 'NOV19_GNAF_PipeSeparatedValue/G-NAF/G-NAF_NOVEMBER_2019/'
                self.FilePath = 'NOV19_GNAF_PipeSeparatedValue{slash}G-NAF{slash}G-NAF_NOVEMBER_2019{slash}Standard{slash}ACT_ADDRESS_ALIAS_psv.psv'
                self.DownURL = 'https://data.gov.au/data/dataset/19432f89-dc3a-4ef3-b943-5326ef1dbecc/resource/4b084096-65e4-4c8e-abbe-5e54ff85f42f/download/nov19_gnaf_pipeseparatedvalue.zip'                
                self.ZipDir = 'csv'
                self.ZipPath ='nov19_gnaf_pipeseparatedvalue.zip'
    
    


    class gnaf_aug_2019:
        """
        ABS Australian Boundary
        """  
        ...
        
        class CSVFormat:
            __slots__= ('Description','Format','FilePath','PathToFiles','DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'gnaf_aug_2019'
                self.Format = 'CSV'
                self.PathToFiles = 'AUG19_GNAF_PipeSeparatedValue{slash}G-NAF_AUGUST_2019'
                self.FilePath = 'AUG19_GNAF_PipeseparatedValue_20190218152308{slash}G-NAF{slash}G-NAF_AUG_2019{slash}Standard{slash}ACT_ADDRESS_ALIAS_psv.psv'
                self.DownURL = 'https://data.gov.au/data/dataset/e1a365fc-52f5-4798-8f0c-ed1d33d43b6d/resource/32be073c-338b-40df-9842-7cd91a25d960/download/aug19_gnaf_pipeseparatedvalue.zip'                
                self.ZipDir = 'csv'
                self.ZipPath ='aug_gnaf_pipeseparatedvalue.zip'

    class gnaf_may_2019:
        
        class CSVFormat:
            __slots__= ('Description','Format','FilePath','PathToFiles','DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'gnaf_may_2019'
                self.Format = 'CSV'
                self.PathToFiles = 'MAY19_GNAF_PipeSeparatedValue_20190521155815{slash}G-NAF{slash}G-NAF_MAY_2019'
                self.FilePath = 'MAY19_GNAF_PipeSeparatedValue_20190521155815{slash}G-NAF{slash}G-NAF_MAY_2019{slash}Standard{slash}ACT_ADDRESS_ALIAS_psv.psv'
                self.DownURL = 'https://data.gov.au/data/dataset/e1a365fc-52f5-4798-8f0c-ed1d33d43b6d/resource/6d481878-82ba-485c-9e01-d1d253383c77/download/may19_gnaf_pipeseparatedvalue_20190521155815.zip'                
                self.ZipDir = 'csv'
                self.ZipPath ='may19_gnaf_pipeseparatedvalue_20190521155815.zip'

    class gnaf_feb_2019:
        
        class CSVFormat:
            __slots__= ('Description','Format','FilePath','PathToFiles','DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'gnaf_feb_2019'
                self.Format = 'CSV'
                self.PathToFiles = 'FEB19_GNAF_PipeSeparatedValue_20190218152308{slash}G-NAF{slash}G-NAF_FEBRUARY_2019'
                self.FilePath = 'FEB19_GNAF_PipeSeparatedValue_20190218152308{slash}G-NAF{slash}G-NAF_FEBRUARY_2019{slash}G-NAF FEBRUARY 2019'
                self.DownURL = 'https://data.gov.au/data/dataset/e1a365fc-52f5-4798-8f0c-ed1d33d43b6d/resource/4251f991-9541-46c2-9a87-5e27f8b0e32d/download/feb19_gnaf_pipeseparatedvalue_20190218152308.zip'                
                self.ZipDir = 'csv'
                self.ZipPath ='feb19_gnaf_pipeseparatedvalue_20190218152308.zip'

