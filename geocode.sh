#!/bin/bash
line_ref=0;
cleaned="addresses_cleaned.txt";
gnaf="gnaf_feb_2020_address_view.csv";
echo "id,cleaned,$(cat $gnaf| head -n 1)" >  addresses_processed.csv;
while IFS= read -r line;
do
  line_ref=$((line_ref+1))
  echo "$line_ref,$line,$(cat $gnaf | grep "$line" | head -n 1)" > tmp_cleaned.csv
  cat tmp_cleaned.csv>> addresses_processed.csv
done < "$cleaned"
