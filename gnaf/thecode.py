from gnaf.parameters import Tables,Defaults

import os,sys,sqlite3,subprocess




class Process:    
    
    class Do_Stuff():
        __slots__ =("SpatialitePath","Slash")
        def __init__(self,splitePath):
            self.SpatialitePath = splitePath
            my_os = str(os.name)
            #print(my_os)
            #ntValues = OSVars.nt()
            #posixValues = OSVars.posix()
            #offValues = Offsets()
        
            if (my_os is 'posix'):
                self.Slash = '/' # posixValues.Slash # '/'
            else:
                self.Slash = '\\'# ntValues.Slash # '\\'
        

        
        def sql_to_db (self,sqltext, db):
            '''
            source: https://stackoverflow.com/questions/44557745/build-sqlite-query-in-python-but-execute-it-using-sqlite3-command-line-program            '''
            thesql  = str(sqltext)
            
            subprocess.check_output(
                ["sqlite3",
                 "{Splite}{slash}{db}.sqlite".\
                 format(db = db,\
                        slash = self.Slash,\
                        Splite = self.SpatialitePath)], input=bytes(thesql.encode("utf-8")))
    class Files:
        def __inte__(self):
            my_os = str(os.name)
            
            if (my_os is 'posix'):
                self.Slash = '/' # posixValues.Slash # '/'
            else:
                self.Slash = '\\'# ntValues.Slash # '\\'

            


        def no_more_spaces_in_path(self,dirPath):
            '''
            # http://pythonfiddle.com/remove-spaces-from-directory-names/
            '''
            
            for dirName in os.listdir(dirPath):
		        if not os.path.isdir(os.path.join(dirPath, dirName)):
			        continue
		        os.rename(os.path.join(dirPath, dirName), os.path.join(dirPath, dirName.replace(' ', '.')))
	        sys.exit(0)
            

    
    class Collect:
        def __init__(self,gnaf_path,sub_dir):
            self.GNAFPath = gnaf_path
            self.subDir = sub_dir
            #print('hello there')

        def pipes_to_comma(self,thefile):
            '''\
            Read a lines from a file line by line into an output file.
            Replace all '|' characters with a ','.
            '''
            srcfile = self.GNAFPath + self.subDir + thefile + '.psv'
            destfile = self.GNAFPath + self.subDir + thefile + '.csv'
            outfile = open(str(destfile), 'w')
            with open(srcfile, 'r', encoding='utf-8') as infile:
                for line in infile:
                    newline = line.replace('|',',')
                    outfile.write(newline)

            outfile.close()
            
        def state_pipes(self,tbl):
            for thestate in tbl.stateList:
                self.pipes_to_comma(tbl.filePiped.format(state = thestate))

        def drop_inp_sql_st(self, tblexp, theState):
            #d = Defaults()
            Def = Defaults()
            expText = tblexp.format(state = theState)
            return expText

        def drop_states_sql_st(self, tbl):
            #d = Defaults()
            Def = Defaults()
            expText =''
            for theState in tbl.stateList:
                expText = expText + self.drop_inp_sql_st(tbl.sqlDropInpTbl,theState) + '\n'
            return expText

        def load_sql_st(self, tblname, theState):
            #d = Defaults()
            Def = Defaults()
            newState = tblname
            if theState is not '':
                newState = tblname.format(state = theState)
            
            expText = Def.sqlLoad.format(table = newState, subdir = self.subDir, filespath = self.GNAFPath) + '\n'
            
            return expText

        def load_states_sql_st(self, tbl):
            #d = Defaults()
            Def = Defaults()
            expText = ""
            for theState in tbl.stateList:
                expText = expText + self.load_sql_st(tbl.filePiped,theState)
            
            return expText
                
    class Collate:

        def create_merge_standard_sql_st(tbl,gnafPath,subDir):
            print(tbl.filePiped)
            c = Process.Collect(gnafPath,subDir)
            c.state_pipes(tbl)
            expText = c.drop_states_sql_st(tbl)
            
            expText = expText + c.load_states_sql_st(tbl)
            
            expText = expText + tbl.sqlDropMrgTbl
            expText = expText + tbl.sqlDropOutTbl
            
            sqlText = '\n' + tbl.sqlStart +'\n'
            
            for thestate in tbl.stateList:
                sqlText = sqlText + tbl.sqlState.format(state = thestate)
                if thestate is not tbl.stateList[-1]:
                    sqlText = sqlText + '\nUNION\n'
                else:
                    sqlText = sqlText + ';\n'
            expText = expText + '\n' + sqlText 
            expText = expText + '\n'+ tbl.sqlTable 
            expText = expText + '\n' + tbl.sqlInsert
            expText = expText + '\n' + tbl.sqlDropMrgTbl
            expText = expText + '\n' + c.drop_states_sql_st(tbl)
            expText = expText + '\nVACUUM;\n'
            
            return expText
        
        def create_merge_auth_sql_st(tbl,gnafPath,subDir):
            print(tbl.filePiped)
            c = Process.Collect(gnafPath,subDir)
            c.pipes_to_comma(tbl.filePiped)
            expText = tbl.sqlDropInpTbl + '\n'
            expText = expText + c.load_sql_st(tbl.filePiped, '') + '\n'
            expText = expText + tbl.sqlDropOutTbl + '\n'
            expText = expText + tbl.sqlTable + '\n'
            expText = expText + tbl.sqlInsert + '\n'
            expText = expText + tbl.sqlDropInpTbl + '\n'
            return expText

        def create_views_sql_st(tbl):
            print(tbl.filePiped)
            
            expText = tbl.sqlDropOutTbl + '\n'
            expText = expText + tbl.sqlView 
            return expText
        
class DataSets:
    
    class Australia:
        """
        ABS Australian Boundary
        """    
        ...
    
        class ShapeFormat:
            __slots__= ('Description','Format','FilePath', 'DownURL', 'ZipDir', 'ZipPath')
            def __init__(self):
                self.Description = 'ABS Australia'
                self.Format = 'Shape'
                self.FilePath = 'shapefiles{slash}AUS_2016_AUST.shp'
                self.DownURL = 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055001_aus_2016_aust_shape.zip&1270.0.55.001&Data%20Cubes&5503B37F8055BFFECA2581640014462C&0&July%202016&24.07.2017&Latest'
                self.ZipDir = 'shapefiles'
                self.ZipPath ='shapefiles{slash}1270055001_aus_2016_aust_shape.zip'
                
    
        class TabFormat:
            __slots__= ('Description','Format','FilePath', 'DownURL', 'ZipDir', 'ZipPath')
            def __init__(self):
                self.Description = 'ABS Australia'
                self.Format = 'Tab'
                self.FilePath = 'tabfiles{slash}AUS_2016_AUST.tab'
                self.DownURL = 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055001_aus_2016_aust_shape.zip&1270.0.55.001&Data%20Cubes&5503B37F8055BFFECA2581640014462C&0&July%202016&24.07.2017&Latest'
                self.ZipDir = 'tabfiles'
                self.ZipPath ='tabfiles{slash}1270055001_aus_2016_aust_tab.zip'
                
    class Statistical_Areas_Level_1_2011:

        class ShapeFormat:
            __slots__= ('Description','Format','FilePath', 'DownURL', 'ZipDir', 'ZipPath')
            def __init__(self):
                self.Description = '2011 ABS Statistical Areas Level 1'
                self.Format = 'Shape'
                self.FilePath = 'shapefiles{slash}SA1_2011_AUST.shp'
                self.DownURL = 'http://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&1270055001_sa1_2011_aust_shape.zip&1270.0.55.001&Data%20Cubes&24A18E7B88E716BDCA257801000D0AF1&0&July%202011&23.12.2010&Latest'
                self.ZipDir = 'shapefiles'
                self.ZipPath ='shapefiles{slash}1270055001_sa1_2011_aust_shape.zip'
                
    class Statistical_Areas_Level_1_2016:

        class ShapeFormat:
            __slots__= ('Description','Format','FilePath', 'DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'ABS Australia'
                self.Format = 'Shape'
                self.FilePath = 'shapefiles{slash}SA1_2011_AUST.shp'
                self.DownURL = 'http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055001_sa1_2016_aust_tab.zip&1270.0.55.001&Data%20Cubes&39A556A0197D8C02CA257FED00140567&0&July%202016&12.07.2016&Latest'
                self.ZipDir = 'shapefiles'
                self.ZipPath ='shapefiles{slash}1270055001_sa1_2011_aust_shape.zip'
                
    class AGIL_Dataset:
        
        class CSVFormat:
            __slots__= ('Description','Format','FilePath', 'DownURL', 'ZipDir', 'ZipPath')
            
            def __init__(self):
                self.Description = 'AGIL DataSet'
                self.Format = 'CSV'
                self.FilePath = 'csv{slash}agil_locations20190208.csv'
                self.DownURL = 'https://data.gov.au/dataset/34b1c164-fbe8-44a0-84fd-467dba645aa7/resource/625e0a41-6a30-4c11-9a20-ac64ba5a1d1f/download/agil_locations20190208.csv'                
                self.ZipDir = 'csv'
                self.ZipPath =''
