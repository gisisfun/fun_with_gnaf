from gnaf.parameters import Tables,Defaults
from gnaf.thecode import Process
d = Defaults()

#upd = 'UPDATE'
#
#print(p.sqlStart)
#
#    print(p.sqlState.format(state = thestate))
#    if thestate is not d.states8[-1]:
#        print(upd)
#    else:
#        print(';')
p = Tables.Standard.ADDRESS_ALIAS()
c = Process.Collect('AUG19_GNAF_PipeSeparatedValue/G-NAF_AUGUST_2019/','Standard/')
for thestate in d.states8:
    print(thestate)
    c.pipes_to_comma(p.filePiped.format(state = thestate))


#
Process.Collate.create_sql(d,p)