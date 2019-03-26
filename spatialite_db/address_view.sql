CREATE VIEW ADDRESS_VIEW

AS

SELECT
(BUILDING_NAME || " " || 
 NUMBER_FIRST || " " || 
 STREET_NAME || " " || 
 LOCALITY_NAME || " " ||
 STATE_ABBREVIATION || " " || 
 POSTCODE  ) as AddressText
AD.address_detail_pid as ADDRESS_DETAIL_PID,
AD.street_locality_pid as STREET_LOCALITY_PID,
AD.locality_pid as LOCALITY_PID,
AD.building_name as BUILDING_NAME,

AD.lot_number_prefix as LOT_NUMBER_PREFIX,
AD.lot_number as LOT_NUMBER,
AD.lot_number_suffix as LOT_NUMBER_SUFFIX,

FTA.name as FLAT_TYPE,
AD.flat_number_prefix as FLAT_NUMBER_PREFIX,
AD.flat_number as FLAT_NUMBER,
AD.flat_number_suffix as FLAT_NUMBER_SUFFIX,

LTA.name as LEVEL_TYPE,
AD.level_number_prefix as LEVEL_NUMBER_PREFIX,
AD.level_number as LEVEL_NUMBER,
AD.level_number_suffix as LEVEL_NUMBER_SUFFIX,

AD.number_first_prefix as NUMBER_FIRST_PREFIX,
AD.number_first as NUMBER_FIRST,
AD.number_first_suffix as NUMBER_FIRST_SUFFIX,
AD.number_last_prefix as NUMBER_LAST_PREFIX,
AD.number_last as NUMBER_LAST,
AD.number_last_suffix as NUMBER_LAST_SUFFIX,

SL.street_name as STREET_NAME,
SL.street_class_code as STREET_CLASS_CODE,
SCA.name as STREET_CLASS_TYPE,
SL.street_type_code as STREET_TYPE_CODE,
SL.street_suffix_code as STREET_SUFFIX_CODE,
SSA.name as STREET_SUFFIX_TYPE,

L.locality_name as LOCALITY_NAME,

ST.state_abbreviation as STATE_ABBREVIATION,

AD.postcode as POSTCODE,

ADG.latitude as LATITUDE,
ADG.longitude as LONGITUDE,
GTA.name as GEOCODE_TYPE,

AD.confidence as CONFIDENCE,

AD.alias_principal as ALIAS_PRINCIPAL,
AD.primary_secondary as PRIMARY_SECONDARY,

AD.legal_parcel_id as LEGAL_PARCEL_ID,

AD.date_created as DATE_CREATED

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
