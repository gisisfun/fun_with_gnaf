# fun_with_gnaf
Lets Build an SQLite3 database with the PSMA G-NAF data set

[When documentation completed and] three files are created:
- res_street_locality.csv,
- street_locality.csv,
- locality.csv

in powershell

```
get-content res_street_locality.csv | select-string "PARLIAMENT HOUSE | search-string "ACT"
get-content street_locality.csv | select-string "CAPITAL HILL"
get-content locality.csv | select-string "CAPITAL HILL"
```

in linux

```
cat res_street_locality.csv | grep "PARLIAMENT HOUSE" | grep "ACT"
cat street_locality.csv | grep "CAPITAL HILL" 
cat locality.csv | grep "CAPITAL HILL"
```
