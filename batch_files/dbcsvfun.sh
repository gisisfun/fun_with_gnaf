
sed -e "s#changeme1#${1}#g; s#changeme2#${2}#g; s#changeme3#${3}#g;" ../spatialite_db/csvcmds_tmpl.txt >cmds.sh
sh cmds.sh






