class Defaults:
    """
    """
    ...

    __slots__ = ("gnaf_path",'states9','states8')
    
    def __init__(self):
        self.gnaf_path = ''
        self.states9 = ['NSW','VIC','QLD','SA','WA','TAS','NT','ACT','OT']
        self.states8 = ['NSW','VIC','QLD','SA','WA','TAS','NT','ACT']
        
        
        
class Tables:
    
    class Standard:
    
    
        class ADDRESS_ALIAS:
            __slots__ = ("filePiped","sqlDropTbl","sqlDropImport","sqlStart","sqlState","sqlUnion", "sqlInsert", "sqlTable")
        
            def __init__(self):
                self.filePiped = '{state}_ADDRESS_ALIAS_psv'
                self.sqlDropTbl = 'DROP TABLE IF EXISTS "ADDRESS_ALIAS_SRC";'
                self.sqlStart = 'CREATE TABLE "ADDRESS_ALIAS_SRC" AS'
                self.sqlState = """SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment
FROM {state}_ADDRESS_ALIAS_psv"""
                self.sqlTable = """CREATE TABLE ADDRESS_ALIAS (
 ogc_fid integer,
 address_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 principal_pid varchar(15) NOT NULL,
 alias_pid varchar(15) NOT NULL,
 alias_type_code varchar(10) NOT NULL,
 alias_comment varchar(200)
);"""
                sql_insert = """INSERT INTO ADDRESS_ALIAS SELECT
 ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment
FROM ADDRESS_ALIAS_SRC;"""
                self.sqlDropImport = 'DROP TABLE IF EXISTS "{state}_ADDRESS_ALIAS_psv";'
            
            
        
                
        class Authority_Code:
            
            class ADDRESS_ALIAS_TYPE_AUT:
                __slots__ = ("sqlDropTbl", "sqlTable","sqlInsert","sqlDropImport")
        
                def __init__(self):
                    self.sqlDropTbl = 'DROP TABLE if exists "ADDRESS_ALIAS_TYPE_AUT";'
                    self.sqlTable = """
CREATE TABLE ADDRESS_ALIAS (
 ogc_fid integer,
 address_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 principal_pid varchar(15) NOT NULL,
 alias_pid varchar(15) NOT NULL,
 alias_type_code varchar(10) NOT NULL,
 alias_comment varchar(200)
);"""
                    sqlInsert = """INSERT INTO ADDRESS_ALIAS_TYPE_AUT
SELECT ogc_fid,code,name,description
FROM authority_code_address_alias_type_aut_psv;
"""
                    self.sqlDropImport = 'DROP TABLE if exists "authority_code_address_alias_type_aut_psv";'
                
            class ADDRESS_CHANGE_TYPE_AUT:
                __slots__ = ("sqlDropTbl", "sqlTable","sqlInsert","sqlDropImport")
        
                def __init__(self):
                    self.sqlDropTbl = 'DROP TABLE if exists "ADDRESS_CHANGE_TYPE_AUT";'
                    self.sqlTable = """
CREATE TABLE ADDRESS_CHANGE_TYPE_AUT (
 ogc_fid integer,
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);"""
                    sqlInsert = """
INSERT INTO ADDRESS_CHANGE_TYPE_AUT
SELECT ogc_fid,code,name,description
FROM authority_code_address_change_type_aut_psv;"""
                    self.sqlDropImport = 'DROP TABLE if exists "authority_code_address_change_type_aut_psv";'
