# fun_with_gnaf
Lets Build an SQLite3 database with the PSMA G-NAF data set

in powershell

get-content gnaf_feb_2018.csv | select-string "SYDNEY NSW" | search-string "OPERA HOUSE"

in linux

cat gnaf_feb_2018.csv | grep "SYDNEY NSW" | grep "OPERA HOUSE"
