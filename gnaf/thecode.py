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
    
    class Collate:

        def create_sql(d,t):
            #d = Defaults()
            upd = 'UPDATE'
            print(t.sqlStart)
            for thestate in d.states8:
                print(t.sqlState.format(state = thestate))
                if thestate is not d.states8[-1]:
                    print(upd)
                else:
                    print(';')

        