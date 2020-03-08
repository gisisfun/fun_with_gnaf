# Fun with G-NAF
**Introduction**

Using the Geospatial National Address File (G-NAF) can be fun and enjoyable experience once you see how it works outside of the Value Added Reseller (VAR) environment. The code here can be used to gain this knowledge. 

The reason people choose the G_NAF File is beacuse it maganges the issues of of complexity when it comes to how people describe their location by a mail delivery address. This makes the file complex. Organisations purchase softeare to further assist with this complexity.

Location source from the G-NAF file on whole are 'accurate' relative to the environment the location data was collected. Not all G-NAF file locations match the ground truth locations due to a range of factors. 

The ability for an organisation to say that the supplied software is being used to produce correct results is based on the level of understanding the the underlying G-NAF File and changes applied it over time by staff of the organstsaion. 

Further information can be found at the PSMA website: 
https://psma.com.au/wp-content/uploads/2019/08/G-NAF-Product-Description.pdf


**Geospatial National Address File (G-NAF)**

The 'file' in reality 38 3rd Nominal Form (3NF) tables ' These tables are aggregated into a lesser number of tables by the code following. At this point it is still not a file. These aggregated tables can reconstructed to conform to the address content you are working with. Normally this task is made easier for organsiations by Value Added Resellers (VAR) but a full understanding of the wide range of the G-NAF File makes hard to understand what is, how it works and what your geocoding software delivers to you. The G-NAF File is complex beacuse addresses usage and collection are subject a wide range of variation.

On 26 February 2016 the G-NAF File was made open source by the Australian Government. The data set is available for download on the data.gov.au website. Prior to this date all use of the address file data was licensed to owner of the VAR software license and G-NAF license fee.

People and data suppliers have their own preferences that influence how data is supplied to your geocoding software and data supplied to the Public Sector Mapping Authority (PSMA) for inclusing the the G-NAF file respectively. The G-NAF file allows for a wide range of variation. Address data is collected from Local Government Authorities (LGA) and contributing organisations for inclusion in periodic releases to VARs or available from the Public Sector Mapping Authority (PSMA) Online acccess systems. These data are collected and subject to local conditions that vary over the country. Addresss locations are measured from a range of reference points on the ground and a level of certainty.

**Non-Standard Addresses Used to Find Standard Addresses**

Addresses vary in content from the 'standard' have been supported by the by the G-NAF File, Documented varation in address content is used to assign the the values of the 'standard' address:

- use of conforming to the standard street (STREET_LOCALITY) suburb (LOCALITY), state (STATE) and postcodes (ADDRESS_DETAIL) names.
- use of known aliases for street (STREET_LOCALIITY_ALIAS), suburb (LOCALITY_ALIAS), state (STATE) and postcodes (ADDRESS_DETAIL) names.
- use of neiighbouring or better known suburb (LOCALITY_NEIGHBOUR) state (STATE) and postcodes (ADDRESS_DETAIL) names.

All of the tthe ables in the G-NAF File are used in the VAR provided address geocoding software. This software is designed to fit into the environment of an organisation without the need to write the code. 

Post offices and rural addresses do not comply with the Australian Standard for addresses or define a physical loction but refer to where mail is physically delivered.

*ADDRESS_DETAIL*

This is where the process starts. The rest of the address is connected by the contents of this table. Using the range of address   data variations in address content you can recronstruct what a reference set of address for address geocoding. 

*LOCAILITY_ALIAS and related tables*

```
CREATE VIEW ALIAS_LOCALITY_VIEW AS
SELECT Loc.locality_pid as locality_pid,
Loc.locality_name as locality_name,
Ste.state_abbreviation as state,
Loc.primary_postcode as postcode,
Loc_ALias.locality_alias_pid as alias_locality_pid,
Loc_Alias.name as alias_locality_name
from [LOCALITY_ALIAS] as Loc_Alias 
inner JOIN [LOCALITY] as Loc
ON Loc.locality_pid = Loc_ALias.locality_pid
join [STATE] as Ste
on Loc_Alias.state_pid = Ste.state_pid
where locality_name = 'LYNEHAM'
order by locality_pid
```

|locality_pid|locality_name|alias_locality_pid|alias_locality_name|
|:-----------|:------------|:-----------------|:------------------|
|ACT101|LYNEHAM|24780|MITCHELL|
|ACT101|LYNEHAM|428425|CANBERRA CENTRAL|

Known Aliases are names that are in use but not officially recognised as the correct suburb name.

*LOCALITY_NEIGHBOUR and related tables*

```
CREATE VIEW NEIGHBOUR_LOCALITY_VIEW AS
SELECT Loc.locality_name as locality_name,
Loc_Neighbour.locality_pid as locality_pid,
Loc_Neighbour.locality_neighbour_pid as locality_neighbour_pid,
Loc_Neighbour.neighbour_locality_pid as neighbour_locality_pid
from [LOCALITY_NEIGHBOUR] as Loc_Neighbour 
inner JOIN [LOCALITY] as Loc
ON Loc.locality_pid = Loc_Neighbour.neighbour_locality_pid
order by neighbour_locality_pid

CREATE VIEW NEIGHBOUR_LOCALITY_LIST_VIEW AS
SELECT NLoc.locality_neighbour_pid as locality_neighbour_pid,
NLoc.neighbour_locality_pid as std_neighbour_locality_pid,
NLoc.locality_name as std_locality_name,
NLoc.locality_pid as nbr_locality_pid,
Loc.locality_name as nbr_locality_name
from
[NEIGHBOUR_LOCALITY_VIEW] as NLoc
inner join [LOCALITY] as Loc on
Nloc.locality_pid = Loc.locality_pid
order by std_neighbour_locality_pid
```

| locality_neighbour_pid | std_neighbour_locality_pid | std_locality_name | nbr_locality_pid|nbr_locality_name |
| :--------------------- | :------------------------- | :---------------- | :--------------- | :-------------- |
| 258771 | ACT101 | LYNEHAM | ACT553 | KALEEN |
| 258829 | ACT101 | LYNEHAM | ACT701 | MITCHELL |
| 258862 | ACT101 | LYNEHAM | ACT103 | O'CONNOR |
| 258949 | ACT101 | LYNEHAM | ACT125 | WATSON |
| 258986 | ACT101 | LYNEHAM | ACT914 | GUNGAHLIN |
| 259187 | ACT101 | LYNEHAM | ACT106 | BRADDON |
| 259193 | ACT101 | LYNEHAM | ACT555 | BRUCE |
| 259266 | ACT101 | LYNEHAM | ACT102 | DICKSON |
| 259407 | ACT101 | LYNEHAM | ACT124 | DOWNER |
| 259474 | ACT101 | LYNEHAM | ACT105 | TURNER |

If the person providing the address prefers a different or better suburn to used for their mail deliveries other than the rela suburb this list can narrow down what the corrected addres should be recorded.

**Not All Locations Are Actual Locations**

Once you have certainty that the correct address record with a corresponding latitude and longitude has been chosen a better understanding of why some latitude and longitude locations where misrepresented (the dot is in the wrong place on the map and/or on the ground).

Survey methodology is used to collect and manage location data and positional accuracy issues. The methodology provides that the location and some kind of description defining the tolerance of postional error of the collected location.  


*GEOCODE_RELIABILITY_AUT*

|code|name|description|
|:----|:-----------|:--------------------------------------------------------------------------------------------|
|1|SURVEYING STANDARD|GEOCODE ACCURACY RECORDED TO APPROPRIATE SURVEYING STANDARD|
|2|WITHIN ADDRESS SITE BOUNDARY OR ACCESS POINT|GEOCODE ACCURACY SUFFICIENT TO PLACE CENTROID WITHIN ADDRESS SITE BOUNDARY OR ACCESS POINT|
|3|NEAR (OR POSSIBLY WITHIN) ADDRESS SITE BOUNDARY|GEOCODE ACCURACY SUFFICIENT TO PLACE CENTROID NEAR (OR POSSIBLY WITHIN) ADDRESS SITE BOUNDARY|
|4|UNIQUE ROAD FEATURE|GEOCODE ACCURACY SUFFICIENT TO ASSOCIATE ADDRESS SITE WITH A UNIQUE ROAD FEATURE|
|5||UNIQUE LOCALITY OR NEIGHBOURHOOD|GEOCODE ACCURACY SUFFICIENT TO ASSOCIATE ADDRESS SITE WITH A UNIQUE LOCALITY OR NEIGHBOURHOOD|
|6|UNIQUE REGION|GEOCODE ACCURACY SUFFICIENT TO ASSOCIATE ADDRESS SITE WITH A UNIQUE REGION|


*GEOCODED_LEVEL_TYPE_AUT*

|code|name|description|
|:---|:------------|:----------------|
|0|NO GEOCODE|NO GEOCODE|
|1|NO LOCALITY|NO STREET|
|2|NO LOCALITY|STREET|
|3|NO LOCALITY|STREET|
|4|LOCALITY|NO STREET|
|5|LOCALITY|NO STREET|
|6|LOCALITY|STREET|
|7|LOCALITY|STREET|


*GEOCODE_TYPE_AUT*

|code|name|description|
|:---|:------------|:--------------------------------------------------------------------------------------------|
|BAP|BUILDING ACCESS POINT|POINT OF ACCESS TO THE BUILDING.|
|BC|BUILDING CENTROID|POINT AS CENTRE OF BUILDING AND LYING WITHIN ITS BOUNDS (E.G. FOR U-SHAPED BUILDING).|
|CDF|CENTRE-LINE DROPPED FRONTAGE|A POINT ON THE ROAD CENTRE-LINE OPPOSITE THE CENTRE OF THE ROAD FRONTAGE OF AN ADDRESS SITE.|
|DF|DRIVEWAY FRONTAGE|CENTRE OF DRIVEWAY ON ADDRESS SITE FRONTAGE.|
|EA|EMERGENCY ACCESS|SPECIFIC BUILDING OR PROPERTY ACCESS POINT FOR EMERGENCY SERVICES.|
|EAS|EMERGENCY ACCESS SECONDARY|SPECIFIC BUILDING OR PROPERTY SECONDARY ACCESS POINT FOR EMERGENCY SERVICES.|
|FDA|FRONT DOOR ACCESS|FRONT DOOR OF BUILDING.|
|FC|FRONTAGE CENTRE|POINT ON THE CENTRE OF THE ADDRESS SITE FRONTAGE.|
|FCS|FRONTAGE CENTRE SETBACK|A POINT SET BACK FROM THE CENTRE OF THE ROAD FRONTAGE WITHIN AN ADDRESS SITE.|
|LB|LETTERBOX|PLACE WHERE MAIL IS DEPOSITED.|
|PAP|PROPERTY ACCESS POINT|ACCESS POINT (CENTRE OF) AT THE ROAD FRONTAGE OF THE PROPERTY.|
|PAPS|PROPERTY ACCESS POINT SETBACK|A POINT SET BACK FROM THE (CENTRE OF TH"string".ToUpper()E) ACCESS POINT AT THE ROAD FRONTAGE OF THE PROPERTY.|
|PC|PROPERTY CENTROID|POINT OF CENTRE OF PARCELS MAKING UP A PROPERTY AND LYING WITHIN ITS BOUNDARIES (E.G. FOR L-SHAPED PROPERTY).|
|PCM|PROPERTY CENTROID MANUAL|POINT MANUALLY PLACED APPROXIMATELY AT CENTRE OF PARCELS MAKING UP A PROPERTY AND LYING WITHIN ITS BOUNDARIES (E.G. FOR L-SHAPED PROPERTY).|
|UC|UNIT CENTROID|POINT AT CENTRE OF UNIT AND LYING WITHIN ITS BOUNDS (E.G. FOR U-SHAPED UNIT).|
|UCM|UNIT CENTROID MANUAL|POINT MANUALLY PLACED APPROXIMATELY AT CENTRE OF UNIT AND LYING WITHIN ITS BOUNDS (E.G. FOR U-SHAPED UNIT).|
|GG|GAP GEOCODE|POINT PROGRAMMATICALLY ALLOCATED DURING THE G-NAF PRODUCTION PROCESS PROPORTIONALLY BETWEEN ADJACENT ADDRESS LOCATIONS (BASED ON NUMBER_FIRST).|
|WCP|WATER CONNECTION POINT|WATER CONNECTION POINT (E.G. BOX|
|WM|WATER METER|WATER METER POINT (E.G. BOX|
|SCP|SEWERAGE CONNECTION POINT|SEWERAGE CONNECTION POINT (E.G. BOX|
|GCP|GAS CONNECTION POINT|GAS CONNECTION POINT (E.G. BOX|
|GM|GAS METER|GAS METER POINT (E.G. BOX|
|TCP|TELEPHONE CONNECTION POINT|TELEPHONE CONNECTION POINT (E.G. BOX|
|ECP|ELECTRICITY CONNECTION POINT|ELECTRICITY CONNECTION POINT (E.G. BOX|
|EM|ELECTRICITY METER|ELECTRICITY METER POINT (E.G. BOX|
|ICP|INTERNET CONNECTION POINT|INTERNET CONNECTION POINT (E.G. BOX|
|UNK|UNKNOWN|THE TYPE OF REAL WORLD FEATURE THE POINT REPRESENTS IS NOT KNOWN.|
|STL|STREET LOCALITY|POINT REPRESENTING THE EXTENT OF A STREET WITHIN A LOCALITY|
|LOC|LOCALITY|POINT REPRESENTING A LOCALITY

**Flats/Units**

Flat/Unit dwellings share the same location latitude/longitude with their own address as a primary address for a single unit dweling (a house, townhouse). the PRIMARY_SECONDARY table holds this information.

*SECONDARY_VIEW*

```
CREATE VIEW SECONDARY_VIEW AS
SELECT PS.primary_secondary_pid as ps_primary_secondary_pid, PS.primary_pid as ps_primary_pid, PS.secondary_pid as ps_secondary_pid,
AD.address_detail_pid as ad_address_detail_pid,
PSJT.name as ps_join_type
FROM [PRIMARY_SECONDARY] AS PS
JOIN [ADDRESS_DETAIL] as AD ON
(PS.secondary_pid = AD.address_detail_pid) and (AD.primary_secondary = 'S')
join [PS_JOIN_TYPE_AUT] as PSJT
ON PS.ps_join_type_code = PSJT.code
```


|ps_primary_secondary_pid|ps_primary_pid|ps_secondary_pid|ad_address_detail_pid|ps_join_type|
|:----------------------|:--------------|:---------------|:--------------------|:-----------|
|ACT10077665|GAOT_718908063|GAOT_718908062|GAOT_718908062|AUTO|
|ACT10077668|GAACT714848778|GAACT718909697|GAACT718909697|AUTO|
|ACT10077669|GAACT714848778|GAACT718909698|GAACT718909698|AUTO|
|ACT10077670|GAACT714848778|GAACT718909699|GAACT718909699|AUTO|
|ACT10077675|GAACT714881052|GAACT718909690|GAACT718909690|AUTO|
|ACT10077676|GAACT714884695|GAACT718908557|GAACT718908557|AUTO|
|ACT10077677|GAACT714884695|GAACT718908558|GAACT718908558|AUTO|
|ACT10077678|GAACT714884695|GAACT718908559|GAACT718908559|AUTO|
|ACT10077679|GAACT714884695|GAACT718908560|GAACT718908560|AUTO|
|ACT10077680|GAACT714884695|GAACT718908561|GAACT718908561|AUTO|

**Address Binning and  Customised Standard and Authority Code Tables**
Based on analysis of address content the processing of addresses is broken up into separate 'bins' with fit for purpose reference address content. These bins form part of the workflow.

Addresses are matched to a combination of non-standard street/locality including prefixes/suffixes/values in Authority Code files that can hold custom values.

The Value Added Reseller (VAR) provides the organisation with ability to customise the bins, Application Program Interfaces (APIs) connect the G-NAF File, Address text preprocessing,address matching services and updates to G-NAF File.


**Over to You**

Lets Build an SqLite3 database with the PSMA G-NAF data set. The Python code stores all of the SQL code that is executed by the Sqlite3 appplication. 
*If you already have the fies output the skip this section*.

```
python3 demo.py

```
- res_street_locality.csv,
- street_locality.csv,
- locality.csv

```
sqlite3 ../spatialite_db/db.sqlite
.mode csv"string".ToUpper()
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
get-content addresses_raw.txt | % {$_.ToUpper()} | % {$_.replace("/"," ")} |% {$_.replace(" LOOP "," LOOP ")}|% {$_.replace(" RISE "," RISE ")}|% {$_.replace(" ARC "," ARCADE ")}|% {$_.replace(" ESP "," ESPLANADE ")}|% {$_.replace(" CV "," COVE ")}|% {$_.replace(" CRES "," CRESCENT ")}|% {$_.replace(" CR "," CRESCENT ")}|% {$_.replace(" ST "," STREET ")}|% {$_.replace(" RD "," ROAD ")}|% {$_.replace(" AVE "," AVENUE ")}|% {$_.replace(" PL "," PLACE ")}|% {$_.replace(" CRT "," COURT ")}|% {$_.replace(" CT "," COURT ")}|% {$_.replace(" DR "," DRIVE ")}|% {$_.replace(" TCE "," TERRACE ")}|% {$_.replace(" PDE "," PARADE ")}|% {$_.replace(" CCT "," CIRCUIT ")}|% {$_.replace(" CRST "," CREST ")}|% {$_.replace(" LA "," LANE ")}|% {$_.replace(" WAY "," WAY ")}|% {$_.replace(" GDN "," GARDENS ")}|% {$_.replace(" GDNS "," GARDENS ")}|% {$_.replace(" CL "," CLOSE ")}|% {$_.replace(" HWY "," HIGHWAY ")}|% {$_.replace(" CCS "," CIRCUS ")}|% {$_.replace(" CCL "," CIRCLE ")}|% {$_.replace(" BVD "," BOULEVARD ")}|% {$_.replace(" BLVD "," BOULEVARD ")}|% {$_.replace("  " , " ")} | out-file addresses_cleaned.txt
```
*Let's Geocode addresses and record the output in another file*
```
$line_ref = 0;echo "" | Out-File -FilePath addresses_processed.txt;foreach($line in Get-Content .\addresses_cleaned.txt){ $line_ref++;$stext=" "+$line;$text=""; $results = get-content gnaf_feb_2020_address_view.csv | select-string $text| select -first 1 ;$text="{0:0}" -f $line_ref+","+$line+"," + $results; echo $text| Out-File -FilePath addresses_processed.txt -Append}
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
Sea Also
https://github.com/minus34/gnaf-loader/blob/master/load-gnaf.py
https://github.com/Zeppelin-and-Pails/Albatros
https://github.com/data61/gnaf
https://github.com/AGLDWG/gnaf-dataset
https://github.com/HughParsonage/PSMA


