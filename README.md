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

in linux shell

```
cat res_street_locality.csv | grep "PARLIAMENT HOUSE" | grep "ACT"
cat street_locality.csv | grep "CAPITAL HILL" 
cat locality.csv | grep "CAPITAL HILL"
```
in R

```
library(readr)
res_street_locality <- read_csv("res_street_locality.csv")
res_street_locality[grep('CAPTIAL HILL',res_street_locality$AddressText),]

street_locality <- read_csv("street_locality.csv")
street_locality[grep('CAPTIAL HILL',street_locality$AddressText),]

locality <- read_csv("locality.csv")
locality[grep('CAPTIAL HILL',locality$AddressText),]
```
