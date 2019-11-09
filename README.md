# Fun with G-NAF
**Introduction**

Using the Geospatial National Address File (G-NAF) can be fun and enjoyable experience once you see how it works outside of the Value Added Reseller (VAR) environment. The code here can be used to gain this knowledge. 

**Geospatial National Address File (G-NAF)**

The 'file' in reality 38 3rd Nominal Form (3NF) tables ' These tables are aggregated into a lesser number of tables by the code following. At this point it is still not a file. These aggregated tables can reconstructed to conform to the address content you are working with. Normally this task is made easier for organsiations by Value Added Resellers (VAR) but a full understanding of the wide range of the G-NAF File makes hard to understand what is, how it works and what your geocoding software delivers to you. The G-NAF File is complex beacuse addresses usage and collection are subject a wide range of variation.

On 26 February 2016 the G-NAF File was made open source by the Australian Government. The data set is available for download on the data.gov.au website. Prior to this date all use of the address file data was licensed to owner of the VAR software license and G-NAF license fee.

People and data suppliers have their own preferences that influence how data is supplied to your geocoding software and data supplied to the Public Sector Mapping Authority (PSMA) for inclusing the the G-NAF file respectively. The G-NAF file allows for a wide range of variation. Address data is collected from Local Government Authorities (LGA) and contributing organisations for inclusion in periodic releases to VARs or available from the Public Sector Mapping Authority (PSMA) Online acccess systems. These data are collected and subject to local conditions that vary over the country. Addresss locations are measured from a range of reference points on the ground and a level of certainty.

**Addresses are Non-Standard**

Addresses vary in content from the 'standard' have been supported by the by the G-NAF File:

- use of conforming to the standard street and suburb (LOCALITY) names.
- use of knwon aliases for suburb (LOCALITY_ALIAS) names.
- use of neiighbouring or better known suburb (LOCALITY_NEIGHBOUR) names.

Post offices and rural addresses do not comply with the Australian Standard for addresses or define a physical loction but refer to where mail is physically delivered.

*LOCALITY_NEIGHBOUR and related tables in action*

| locality_neighbour_pid | std_neighbour_locality_pid | std_locality_name | nbr_locality_pid|nbr_locality_name |
| :--------------------- | :------------------------- | :---------------- | :--------------------------------- |
| 258771 | ACT101 | LYNEHAM | ACT553 | KALEEN |
| 258829 | ACT101 | LYNEHAM | ACT701 | MITCHELL |
| 258862 | ACT101 | LYNEHAM |ACT103 | O'CONNOR|
| 258949 | ACT101 | LYNEHAM |ACT125 | WATSON|
| 258986 | ACT101 | LYNEHAM |ACT914 | GUNGAHLIN|
| 259187 | ACT101 | LYNEHAM |ACT106 | BRADDON|
| 259193 | ACT101 | LYNEHAM |ACT555 | BRUCE|
| 259266 | ACT101 | LYNEHAM |ACT102 | DICKSON|
| 259407 | ACT101 | LYNEHAM | ACT124 | DOWNER |
| 259474 |ACT101 | LYNEHAM |ACT105 | TURNER |

**Over to You**

Lets Build an SqLite3 database with the PSMA G-NAF data set. 
*If you already have the fies output the skip this section*.

```
python3 demo.py

```
- res_street_locality.csv,
- street_locality.csv,
- locality.csv

```
sqlite3 ../spatialite_db/db.sqlite
.mode csv
.headers on
output ../res_street_locality.csv
select * from ADDRESS_VIEW;
output ../street_locality.csv
select * from STREET_LOCALITY_VIEW;
output ../locality.csv
select * from LOCALITY_VIEW;
.quit
```



**Accessing Data Output of Code**

*in powershell*

```
get-content res_street_locality.csv | select-string "PARLIAMENT HOUSE" | select-string "ACT"
get-content street_locality.csv | select-string "CAPITAL HILL"
get-content locality.csv | select-string "CAPITAL HILL"

```

A DIY Powershell Address Geocoder

*Let's clean the input file*
```
get-content rawaddresses.txt | % {$_.replace("/"," ")} |% {$_.replace("cres ","crescent ")} | % {$_.replace(","," ")} |% {$_.replace("st ","street ")} |% {$_.replace("  " , " ")} | out-file myaddresses.txt
```
*Let's Geocode addresses and record the output in another file*
```
echo "" | Out-File -FilePath Process.txt;foreach($line in [System.IO.File]::ReadLines("myaddresses.txt")){ echo $line| Out-File -FilePath Process.txt -Append; get-content res_street_locality.csv | select-string $line| select -first 1 | Out-File -FilePath Process.txt -Append}
```


https://stackoverflow.com/questions/33511772/read-file-line-by-line-in-powershell

*in linux shell*

```
cat res_street_locality.csv | grep "PARLIAMENT HOUSE" | grep "ACT"
cat street_locality.csv | grep "CAPITAL HILL" 
cat locality.csv | grep "CAPITAL HILL"
```
*in R*

```
library(readr)
res_street_locality <- read_csv("res_street_locality.csv")
res_street_locality[grep('CAPTIAL HILL',res_street_locality$AddressText),]

street_locality <- read_csv("street_locality.csv")
street_locality[grep('CAPTIAL HILL',street_locality$AddressText),]

locality <- read_csv("locality.csv")
locality[grep('CAPTIAL HILL',locality$AddressText),]
```
