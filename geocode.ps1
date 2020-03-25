$line_ref = 0;echo "" | Out-File -FilePath addresses_processed.csv;
foreach($line in Get-Content .\addresses_cleaned.txt){ 
  $line_ref++;$text=" ";
  $results = get-content gnaf_feb_2020_address_view.csv |
  select-string $line| select -first 1 ;
  $text="{0:0}" -f $line_ref+","+$line+"," + $results; echo $text|
 Out-File -FilePath addresses_processed.csv -Append
}
