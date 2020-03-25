#!/bin/bash
cat addresses_raw.txt |
grep -e 's:/:\\/:g' |
tr a-z A-Z |
grep -e 's/* / /g' |
grep -e 's/,/ /g' |
grep -e 's/ LOOP / LOOP /g' |
grep -e 's/ RISE / RISE /g' |
grep -e 's/ ARC / ARCADE /g' |
grep -e 's/ ESP / ESPLANADE /g' |
grep -e 's/ CV / COVE /g' |
grep -e 's/ CRES / CRESCENT /g' |
grep -e 's/ CR / CRESCENT /g' |
grep -e 's/ ST / STREET /g' |
grep -e 's/ RD / ROAD /g' |
grep -e 's/ AVE / AVENUE /g' |
grep -e 's/ PL / PLACE /g' |
grep -e 's/ CRT / COURT /g' |
grep -e 's/ CT / COURT /g' |
grep -e 's/ DR / DRIVE /g' |
grep -e 's/ TCE / TERRACE /g' |
grep -e 's/ PDE / PARADE /g' |
grep -e 's/ CCT / CIRCUIT /g' |
grep -e 's/ CRST / CREST /g' |
grep -e 's/ LA / LANE /g' |
grep -e 's/ WAY / WAY /g' |
grep -e 's/ GDN / GARDENS /g' |
grep -e 's/ GDNS /GARDENS /g' |
grep -e 's/ CL / CLOSE /g' |
grep -e 's/ HWY / HIGHWAY /g' |
grep -e 's/ CCS / CIRCUS /g' |
grep -e 's/ CCL / CIRCLE /g'|
grep -e 's/ BVD / BOULEVARD /g' |
grep -e 's/ BLVD / BOULEVARD /g' >
addresses_cleaned.txt
