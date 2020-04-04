$line_ref = 0;echo "id,cleaned,Address_Detail_PID,Street_Locality_PID,Locality_PID,Building_Name,Lot_Number_Prefix,Lot_Number,Lot_Number_Suffix,Flat_Type,Flat_Number_Prefix,Flat_Number,Flat_Number_Suffix,Level_Type,Level_Number,Number_First_Prefix,Number_First,Street_Name,Street_Type_Code,Locality_Name,State_Abbreviation,Postcode,Confidence,AddressText,Latitude,Longitude,Geocode_Type" | Out-File -FilePath addresses_processed.csv;
foreach($line in Get-Content .\addresses_cleaned.txt){ 
  $line_ref++;$text=" ";
  $results = get-content gnaf_feb_2020_address_view.csv |
  select-string $line| select -first 1 ;
  $text="{0:0}" -f $line_ref+","+$line+"," + $results; echo $text|
 Out-File -FilePath addresses_processed.csv -Append
}
