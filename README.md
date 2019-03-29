# fun_with_gnaf
Lets Build an SQLite3 database with the PSMA G-NAF data set

in powershell

get-content gnaf_feb_2018.csv | select-string "PARLIAMENT HOUSE | search-string "ACT"

in linux

cat gnaf_feb_2018.csv | grep "PARLIAMENT HOUSE" | grep "OACT"
