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
gnafP = 'AUG19_GNAF_PipeSeparatedValue/G-NAF_AUGUST_2019/' 
Process.Collate.create_merge_standard_sql_st(Tables.Standard.ADDRESS_ALIAS(),gnafP,'Standard/')
#c.drop_states_sql_st(p)
Process.Collate.create_merge_auth_sql_st(Tables.Authority_Code.ADDRESS_ALIAS_TYPE_AUT(),gnafP,'Authority_Code/')