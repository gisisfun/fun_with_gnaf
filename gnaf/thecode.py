from gnaf.parameters import Tables,Defaults

class Process:    
    
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
                print(thestate)
                self.pipes_to_comma(tbl.filePiped.format(state = thestate))

        def drop_inp_sql_st(self, tblexp, theState):
            #d = Defaults()
            Def = Defaults()
            
            newExp = tblexp.format(state = theState)
            print(newExp)

        def drop_states_sql_st(self, tbl):
            #d = Defaults()
            Def = Defaults()
            
            for theState in tbl.stateList:
                self.drop_inp_sql_st(tbl.sqlDropInpTbl,theState)

        def load_sql_st(self, tblname, theState):
            #d = Defaults()
            Def = Defaults()
            newState = tblname
            if theState is not '':
                newState = tblname.format(state = theState)
            
            print(Def.sqlLoad.format(table = newState, subdir = self.subDir, filespath = self.GNAFPath))


        def load_states_sql_st(self, tbl):
            #d = Defaults()
            Def = Defaults()
            
            for theState in tbl.stateList:
                self.load_sql_st(tbl.filePiped,theState)
                
    class Collate:

        def create_merge_standard_sql_st(tbl,gnafPath,subDir):
            c = Process.Collect(gnafPath,subDir)
            c.state_pipes(tbl)
            c.drop_states_sql_st(tbl)
            c.load_states_sql_st(tbl)
            upd = 'UPDATE'
            print(tbl.sqlDropMrgTbl)
            print(tbl.sqlStart)
            for thestate in tbl.stateList:
                print(tbl.sqlState.format(state = thestate))
                if thestate is not tbl.stateList[-1]:
                    print(upd)
                else:
                    print(';')
            
            print(tbl.sqlTable)
            print(tbl.sqlInsert)
            print(tbl.sqlDropMrgTbl)
            c.drop_states_sql_st(tbl)
        
        def create_merge_auth_sql_st(tbl,gnafPath,subDir):
            c = Process.Collect(gnafPath,subDir)
            c.pipes_to_comma(tbl.filePiped)
            print(tbl.sqlDropImpTbl)

            c.load_sql_st(tbl.filePiped, '')

            print(tbl.sqlDropTbl)

            
            print(tbl.sqlTable)
            print(tbl.sqlInsert)
            print(tbl.sqlDropImpTbl)
#            c.drop_states_sql_st(tbl)