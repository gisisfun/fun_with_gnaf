
$line_ref = 0;$perfect=0;$partial=0;no_match=0;echo "id,cleaned,Address_Detail_PID,Street_Locality_PID,Locality_PID,Building_Name,Lot_Number_Prefix,Lot_Number,Lot_Number_Suffix,Flat_Type,Flat_Number_Prefix,Flat_Number,Flat_Number_Suffix,Level_Type,Level_Number,Number_First_Prefix,Number_First,Street_Name,Street_Type_Code,Locality_Name,State_Abbreviation,Postcode,Confidence,AddressText,Latitude,Longitude,Geocode_Type,Results_Code" | Out-File -FilePath addresses_processed.csv;
foreach($line in Get-Content .\addresses_cleaned.txt){ 
  $line_ref++;$text=" ";
  write-host(" address record: " + $line_ref + " address: " + $line)
  $search_result = get-content gnaf_feb_2020_address_view.csv |
  select-string $line| select -first 1 ;
  $text="{0:0}" -f $line_ref+","+$line+"," + $search_result
  If ($test[$text.length-1] -eq ',') 
    {
      $arr = $text -split ',';
      $addr_trimd = $arr[23].replace('"','').Trim()
      if ($arr[1] -Match $addr_trimd)
         {write-host("perfect match for address: " + $addr_trimd);
          $result_code = 2;
	  $perfect++  
	}
       Else
         {write_host("partial match for address: " + $addr_trimd);
         $result_code = 1;
	 $partial++}
    }
  Else
    {write-host("no match for address: " + $addr_trimd);
    $result_code = 0;
    $no_match++;
    $text=$text+",,,,,,,,,,,,,,,,,,,,,,,,"};
  $processed = $perfect + $partial + $no_match;
  $text = $text + "," + $result_code; 
  echo $text| Out-File -FilePath addresses_processed.csv -Append;
  write-host("full match: " + $perfect + " partial match: " + $partial + " no match: " + $no_match + " total: " + $processed)
}

