# fun_with_gnaf
Lets Build an SQLite3 database with the PSMA G-NAF data set

[When documentation completed and] three files are created:
- res_street_locality.csv,
- street_locality.csv,
- locality.csv

in powershell

```
get-content res_street_locality.csv | select-string "PARLIAMENT HOUSE" | select-string "ACT"
get-content street_locality.csv | select-string "CAPITAL HILL"
get-content locality.csv | select-string "CAPITAL HILL"

```

A DIY Powershell Geocoder

Let's clean the input file
```
get-content rawaddresses.txt | % {$_.replace("/"," ")} |% {$_.replace("cres ","crescent ")} | % {$_.replace(","," ")} |% {$_.replace("st ","street ")} |% {$_.replace("  " , " ")} | out-file myaddresses.txt
```
Let's Geocode addresses
```
echo "" | Out-File -FilePath Process.txt;foreach($line in [System.IO.File]::ReadLines("myaddresses.txt")){ echo $line| Out-File -FilePath Process.txt -Append; get-content res_street_locality.csv | select-string $line| select -first 1 | Out-File -FilePath Process.txt -Append}
```


https://stackoverflow.com/questions/33511772/read-file-line-by-line-in-powershell

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
