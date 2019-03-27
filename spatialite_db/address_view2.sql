
CREATE VIEW ADDRESS_VIEW2

AS

SELECT

AD.address_detail_pid as Address_Detail_PID,
AD.street_locality_pid as Street_Locality_PID,
AD.locality_pid as Locality_PID,
AD.building_name as Building_Name,

AD.lot_number_prefix as Lot_Number_Prefix,
AD.lot_number as Lot_Number,
AD.lot_number_suffix as Lot_Number_Suffix,

FTA.name as Flat_Type,
AD.flat_number_prefix as Flat_Number_Prefix,
AD.flat_number as Flat_Number,
AD.flat_number_suffix as Flat_Number_Suffix,

LTA.name as Level_Type,

AD.level_number as Level_Number,


AD.number_first_prefix as Number_First_Prefix,
AD.number_first as Number_First,

SL.street_name as Street_Name,
SL.street_type_code as Street_Type_Code,

L.locality_name as Locality_Name,

ST.state_abbreviation as State_Abbreviation,

AD.postcode as Postcode,


AD.confidence as Confidence,

(Flat_Type_Code || " " || 
 Flat_Number || " " || 
 Building_Name || " " || 
 Number_First || " " || 
 Street_Name || " " || 
 Street_Type_Code || " " || 
 Locality_Name || " " ||
 State_Abbreviation || " " || 
 Postcode  ) as AddressText,
 ADG.latitude as Latitude,
ADG.longitude as Longitude,
GTA.name as Geocode_Type

FROM
[ADDRESS_DETAIL] as AD 
LEFT JOIN [FLAT_TYPE_AUT] as FTA ON AD.flat_type_code=FTA.code
LEFT JOIN [LEVEL_TYPE_AUT] as LTA ON AD.level_type_code=LTA.code
JOIN [STREET_LOCALITY] as SL ON AD.street_locality_pid=SL.street_locality_pid
LEFT JOIN [STREET_SUFFIX_AUT] as SSA ON SL.street_suffix_code=SSA.code
LEFT JOIN [STREET_CLASS_AUT] as SCA ON SL.street_class_code=SCA.code 
LEFT JOIN [STREET_TYPE_AUT] as STA ON SL.STREET_TYPE_CODE=STA.CODE
JOIN [LOCALITY] as L ON AD.locality_pid= L.locality_pid
JOIN [ADDRESS_DEFAULT_GEOCODE] as ADG ON AD.address_detail_pid=ADG.address_detail_pid
LEFT JOIN [GEOCODE_TYPE_AUT] as GTA ON ADG.geocode_type_code=GTA.code
LEFT JOIN [GEOCODED_LEVEL_TYPE_AUT] as GLTA ON AD.level_geocoded_code=GLTA.code
JOIN [STATE] as ST ON L.state_pid=ST.state_pid

WHERE 
AD.confidence > -1

UNION

SELECT

AD.address_detail_pid as Address_Detail_PID,
AD.street_locality_pid as Street_Locality_PID,
AD.locality_pid as Locality_PID,
AD.building_name as Building_Name,

AD.lot_number_prefix as Lot_Number_Prefix,
AD.lot_number as Lot_Number,
AD.lot_number_suffix as Lot_Number_Suffix,

FTA.name as Flat_Type,
AD.flat_number_prefix as Flat_Number_Prefix,
AD.flat_number as Flat_Number,
AD.flat_number_suffix as Flat_Number_Suffix,

LTA.name as Level_Type,

AD.level_number as Level_Number,


AD.number_first_prefix as Number_First_Prefix,
AD.number_first as Number_First,

SL.street_name as Street_Name,
SL.street_type_code as Street_Type_Code,

L.name as Locality_Name,

ST.state_abbreviation as State_Abbreviation,

AD.postcode as Postcode,


AD.confidence as Confidence,

(Flat_Type_Code || " " || 
 Flat_Number || " " || 
 Building_Name || " " || 
 Number_First || " " || 
 SL.street_name || " " || 
 SL.street_type_code || " " || 
 L.name || " " ||
 State_Abbreviation || " " || 
 AD.postcode  ) as AddressText,
 ADG.latitude as Latitude,
ADG.longitude as Longitude,
GTA.name as Geocode_Type

FROM
[ADDRESS_DETAIL] as AD 
LEFT JOIN [FLAT_TYPE_AUT] as FTA ON AD.flat_type_code=FTA.code
LEFT JOIN [LEVEL_TYPE_AUT] as LTA ON AD.level_type_code=LTA.code
JOIN [STREET_LOCALITY_ALIAS] as SL ON AD.street_locality_pid=SL.street_locality_pid
LEFT JOIN [STREET_SUFFIX_AUT] as SSA ON SL.street_suffix_code=SSA.code
LEFT JOIN [STREET_TYPE_AUT] as STA ON SL.STREET_TYPE_CODE=STA.CODE
JOIN [LOCALITY_ALIAS] as L ON AD.locality_pid= L.locality_alias_pid
JOIN [ADDRESS_DEFAULT_GEOCODE] as ADG ON AD.address_detail_pid=ADG.address_detail_pid
LEFT JOIN [GEOCODE_TYPE_AUT] as GTA ON ADG.geocode_type_code=GTA.code
LEFT JOIN [GEOCODED_LEVEL_TYPE_AUT] as GLTA ON AD.level_geocoded_code=GLTA.code
JOIN [STATE] as ST ON L.state_pid=ST.state_pid

WHERE 
AD.confidence > -1
;