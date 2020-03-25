#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:54:43 2020

@author: pi
"""

in_file =open("addresses_raw.txt","r")

in_text_lines = in_file.readlines()
in_file.close()
out_file = open("addresses_cleaned.txt","w")
for line in in_text_lines:
    ucase = line.upper().upper()
    punct_space = ucase.replace("[,/]"," ")
    more_space = punct_space.replace("\s+ "," ")
    abbrev = more_space.replace(" ST "," STREET ") \
    .replace(" ARC "," ARCADE ") \
    .replace(" ESP "," ESPLANADE ") \
    .replace(" CV "," COVE ") \
    .replace(" CRES "," CRESCENT ") \
    .replace(" CR "," CRESCENT ") \
    .replace(" ST "," STREET ") \
    .replace(" RD "," ROAD ") \
    .replace(" AVE "," AVENUE ") \
    .replace(" PL "," PLACE ") \
    .replace(" CRT "," COURT ") \
    .replace(" CT "," COURT ") \
    .replace(" DR "," DRIVE ") \
    .replace(" TCE "," TERRACE ") \
    .replace(" PDE "," PARADE ") \
    .replace(" CCT "," CIRCUIT ") \
    .replace(" CRST "," CREST ") \
    .replace(" LA "," LANE ") \
    .replace(" WAY "," WAY ") \
    .replace(" GDN "," GARDENS ") \
    .replace(" GDNS "," GARDENS ") \
    .replace(" CL "," CLOSE ") \
    .replace(" HWY "," HIGHWAY ") \
    .replace(" CCS "," CIRCUS ") \
    .replace(" CCL "," CIRCLE ") \
    .replace(" BVD "," BOULEVARD ") \
    .replace(" BLVD "," BOULEVARD ") \
    .replace(" ST "," STREET ") \
    .replace(" MT "," MOUNT ")
    print(abbrev)
    out_file.write(abbrev)


out_file.close()
