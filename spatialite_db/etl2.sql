DROP TABLE IF EXISTS "ADDRESS_ALIAS_SRC";
CREATE TABLE "ADDRESS_ALIAS_SRC" AS
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
NSW_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
ACT_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
VIC_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
QLD_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
SA_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
QLD_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
NT_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
WA_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
TAS_ADDRESS_ALIAS_psv
UNION
SELECT ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment 
FROM 
OT_ADDRESS_ALIAS_psv
;

DROP TABLE if exists "ACT_ADDRESS_ALIAS_psv";
DROP TABLE if exists "NSW_ADDRESS_ALIAS_psv";
DROP TABLE if exists "VIC_ADDRESS_ALIAS_psv";
DROP TABLE if exists "SA_ADDRESS_ALIAS_psv";
DROP TABLE if exists "QLD_ADDRESS_ALIAS_psv";
DROP TABLE if exists "NT_ADDRESS_ALIAS_psv";
DROP TABLE if exists "TAS_ADDRESS_ALIAS_psv";
DROP TABLE if exists "WA_ADDRESS_ALIAS_psv";
DROP TABLE if exists "OT_ADDRESS_ALIAS_psv";
DROP TABLE if exists "ADDRESS_ALIAS";

CREATE TABLE ADDRESS_ALIAS (
 ogc_fid integer,
 address_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 principal_pid varchar(15) NOT NULL,
 alias_pid varchar(15) NOT NULL,
 alias_type_code varchar(10) NOT NULL,
 alias_comment varchar(200)
);
 
INSERT INTO ADDRESS_ALIAS SELECT
 ogc_fid,address_alias_pid,date_created,date_retired,principal_pid,alias_pid,alias_type_code,alias_comment
FROM ADDRESS_ALIAS_SRC; 

DROP TABLE IF EXISTS "ADDRESS_ALIAS_SRC";

DROP TABLE if exists "ADDRESS_ALIAS_TYPE_AUT";

CREATE TABLE ADDRESS_ALIAS_TYPE_AUT (
 ogc_fid integer,
 code varchar(10) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(30)
);

INSERT INTO ADDRESS_ALIAS_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_address_alias_type_aut_psv;

DROP TABLE if exists "authority_code_address_alias_type_aut_psv";

DROP TABLE if exists "ADDRESS_CHANGE_TYPE_AUT";

CREATE TABLE ADDRESS_CHANGE_TYPE_AUT (
 ogc_fid integer,
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);

INSERT INTO ADDRESS_CHANGE_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_address_change_type_aut_psv;

DROP TABLE IF EXISTS "authority_code_address_change_type_aut_psv";
 
DROP TABLE IF EXISTS "ADDRESS_DEFAULT_GEOCODE_SRC";

CREATE TABLE "ADDRESS_DEFAULT_GEOCODE_SRC" AS
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM 
NSW_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM 
ACT_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM 
VIC_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude 
FROM 
QLD_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM 
SA_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM 
QLD_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude 
FROM 
NT_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude 
FROM 
WA_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude 
FROM 
TAS_ADDRESS_DEFAULT_GEOCODE_psv
UNION
SELECT ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude 
FROM 
OT_ADDRESS_DEFAULT_GEOCODE_psv
;
 
DROP TABLE if exists "ACT_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "NSW_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "VIC_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "SA_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "QLD_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "NT_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "TAS_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "WA_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "OT_ADDRESS_DEFAULT_GEOCODE_psv";
DROP TABLE if exists "ADDRESS_DEFAULT_GEOCODE";

CREATE TABLE ADDRESS_DEFAULT_GEOCODE (
 ogc_fid integer,
 address_default_geocode_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 geocode_type_code varchar(4) NOT NULL,
 longitude numeric(11,8),
 latitude numeric(10,8)
);

INSERT INTO ADDRESS_DEFAULT_GEOCODE SELECT
 ogc_fid,address_default_geocode_pid,date_created,date_retired,address_detail_pid,geocode_type_code,longitude,latitude
FROM
 ADDRESS_DEFAULT_GEOCODE_SRC;
 
DROP TABLE IF EXISTS "ADDRESS_DEFAULT_GEOCODE_SRC";

DROP TABLE IF EXISTS "ADDRESS_DETAIL_SRC";

CREATE TABLE "ADDRESS_DETAIL_SRC" AS
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
NSW_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
ACT_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
VIC_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary 
FROM 
QLD_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
SA_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
QLD_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
NT_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary 
FROM 
WA_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
TAS_ADDRESS_DETAIL_psv
UNION
SELECT ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM 
OT_ADDRESS_DETAIL_psv
;
DROP TABLE if exists "ACT_ADDRESS_DETAIL_psv";
DROP TABLE if exists "NSW_ADDRESS_DETAIL_psv";
DROP TABLE if exists "VIC_ADDRESS_DETAIL_psv";
DROP TABLE if exists "SA_ADDRESS_DETAIL_psv";
DROP TABLE if exists "QLD_ADDRESS_DETAIL_psv";
DROP TABLE if exists "NT_ADDRESS_DETAIL_psv";
DROP TABLE if exists "TAS_ADDRESS_DETAIL_psv"; 
DROP TABLE if exists "WA_ADDRESS_DETAIL_psv"; 
DROP TABLE if exists "OT_ADDRESS_DETAIL_psv"; 
DROP TABLE if exists "ADDRESS_DETAIL";

CREATE TABLE ADDRESS_DETAIL (
 ogc_fid integer,
 address_detail_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_last_modified date,
 date_retired date,
 building_name varchar(200),
 lot_number_prefix varchar(2),
 lot_number varchar(5),
 lot_number_suffix varchar(2),
 flat_type_code varchar(7),
 flat_number_prefix varchar(2),
 flat_number numeric(5),
 flat_number_suffix varchar(2),
 level_type_code varchar(4),
 level_number_prefix varchar(2),
 level_number numeric(3),
 level_number_suffix varchar(2),
 number_first_prefix varchar(3),
 number_first numeric(6),
 number_first_suffix varchar(2),
 number_last_prefix varchar(3),
 number_last numeric(6),
 number_last_suffix varchar(2),
 street_locality_pid varchar(15),
 location_description varchar(45),
 locality_pid varchar(15) NOT NULL,
 alias_principal char(1),
 postcode varchar(4),
 private_street varchar(75),
 legal_parcel_id varchar(20),
 confidence numeric(1),
 address_site_pid varchar(15) NOT NULL,
 level_geocoded_code numeric(2) NOT NULL,
 property_pid varchar(15),
 gnaf_property_pid varchar(15),
 primary_secondary varchar(1)
);

INSERT INTO ADDRESS_DETAIL SELECT
 ogc_fid,address_detail_pid,date_created,date_last_modified,date_retired,building_name,lot_number_prefix,lot_number,lot_number_suffix,flat_type_code,flat_number_prefix,flat_number,flat_number_suffix ,level_type_code,level_number_prefix,level_number,level_number_suffix,number_first_prefix,number_first,number_first_suffix,number_last_prefix,number_last,number_last_suffix,street_locality_pid,location_description, locality_pid, alias_principal, postcode, private_street, legal_parcel_id, confidence, address_site_pid, level_geocoded_code, property_pid, gnaf_property_pid,primary_secondary
FROM
 ADDRESS_DETAIL_SRC;

DROP TABLE if exists "ADDRESS_DETAIL_SRC";

DROP TABLE if exists "ADDRESS_FEATURE_SRC";

CREATE TABLE ADDRESS_FEATURE_SRC AS
SELECT address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
NSW_ADDRESS_FEATURE_psv
UNION
SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
ACT_ADDRESS_FEATURE_psv
UNION
SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
VIC_ADDRESS_FEATURE_psv
UNION
SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
QLD_ADDRESS_FEATURE_psv
UNION
SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
SA_ADDRESS_FEATURE_psv
UNION
SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
QLD_ADDRESS_FEATURE_psv
UNION
SELECT address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM  
NT_ADDRESS_FEATURE_psv
UNION
SELECT address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
WA_ADDRESS_FEATURE_psv
UNION
SELECT  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
TAS_ADDRESS_FEATURE_psv
;

DROP TABLE if exists "ACT_ADDRESS_FEATURE_psv";
DROP TABLE if exists "NSW_ADDRESS_FEATURE_psv";
DROP TABLE if exists "VIC_ADDRESS_FEATURE_psv";
DROP TABLE if exists "SA_ADDRESS_FEATURE_psv";
DROP TABLE if exists "QLD_ADDRESS_FEATURE_psv";
DROP TABLE if exists "NT_ADDRESS_FEATURE_psv";
DROP TABLE if exists "TAS_ADDRESS_FEATURE_psv"; 
DROP TABLE if exists "WA_ADDRESS_FEATURE_psv";
DROP TABLE if exists "ADDRESS_FEATURE";

CREATE TABLE ADDRESS_FEATURE (
 address_feature_id varchar(16) NOT NULL,
 address_feature_pid varchar(16) NOT NULL,
 address_detail_pid varchar(15) NOT NULL,
 date_address_detail_created date NOT NULL,
 date_address_detail_retired date,
 address_change_type_code varchar(50)
);

INSERT INTO ADDRESS_FEATURE SELECT
  address_feature_id,address_feature_pid, address_detail_pid,date_address_detail_created, date_address_detail_retired,address_change_type_code 
FROM 
 ADDRESS_FEATURE_SRC;

DROP TABLE if exists "ADDRESS_FEATURE_SRC";

DROP TABLE if exists "ADDRESS_MESH_BLOCK_2011_SRC";

CREATE TABLE "ADDRESS_MESH_BLOCK_2011_SRC" AS
SELECT ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
NSW_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT  ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
ACT_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT  ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
VIC_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
QLD_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT  ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
SA_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT  ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
QLD_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
NT_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
WA_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
TAS_ADDRESS_MESH_BLOCK_2011_psv
UNION
SELECT ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
OT_ADDRESS_MESH_BLOCK_2011_psv
;

DROP TABLE if exists "ACT_ADDRESS_MESH_BLOCK_2011_psv";
DROP TABLE if exists "NSW_ADDRESS_MESH_BLOCK_2011_psv";
DROP TABLE if exists "VIC_ADDRESS_MESH_BLOCK_2011_psv";
DROP TABLE if exists "SA_ADDRESS_MESH_BLOCK_2011_psv";
DROP TABLE if exists "QLD_ADDRESS_MESH_BLOCK_2011_psv";
DROP TABLE if exists "NT_ADDRESS_MESH_BLOCK_2011_psv";
DROP TABLE if exists "TAS_ADDRESS_MESH_BLOCK_2011_psv"; 
DROP TABLE if exists "WA_ADDRESS_MESH_BLOCK_2011_psv"; 
DROP TABLE if exists "OT_ADDRESS_MESH_BLOCK_2011_psv"; 
DROP TABLE if exists "ADDRESS_MESH_BLOCK_2011";

CREATE TABLE ADDRESS_MESH_BLOCK_2011 (
 ogc_fid integer,
 address_mesh_block_2011_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 mb_match_code varchar(15) NOT NULL,
 mb_2011_pid varchar(15) NOT NULL
);

INSERT INTO ADDRESS_MESH_BLOCK_2011 SELECT
  ogc_fid,address_mesh_block_2011_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2011_pid 
FROM 
 ADDRESS_MESH_BLOCK_2011_SRC;

DROP TABLE if exists "ADDRESS_MESH_BLOCK_2011_SRC";

DROP TABLE if exists "ADDRESS_MESH_BLOCK_2016_SRC";

CREATE TABLE "ADDRESS_MESH_BLOCK_2016_SRC" AS
SELECT ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
NSW_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT  ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
ACT_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT  ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
VIC_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
QLD_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT  ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
SA_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT  ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
QLD_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
NT_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
WA_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
TAS_ADDRESS_MESH_BLOCK_2016_psv
UNION
SELECT ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
OT_ADDRESS_MESH_BLOCK_2016_psv
;

DROP TABLE if exists "ACT_ADDRESS_MESH_BLOCK_2016_psv";
DROP TABLE if exists "NSW_ADDRESS_MESH_BLOCK_2016_psv";
DROP TABLE if exists "VIC_ADDRESS_MESH_BLOCK_2016_psv";
DROP TABLE if exists "SA_ADDRESS_MESH_BLOCK_2016_psv";
DROP TABLE if exists "QLD_ADDRESS_MESH_BLOCK_2016_psv";
DROP TABLE if exists "NT_ADDRESS_MESH_BLOCK_2016_psv";
DROP TABLE if exists "TAS_ADDRESS_MESH_BLOCK_2016_psv"; 
DROP TABLE if exists "WA_ADDRESS_MESH_BLOCK_2016_psv"; 
DROP TABLE if exists "OT_ADDRESS_MESH_BLOCK_2016_psv"; 
DROP TABLE if exists "ADDRESS_MESH_BLOCK_2016";

CREATE TABLE ADDRESS_MESH_BLOCK_2016 (
 ogc_fid integer,
 address_mesh_block_2016_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_detail_pid varchar(15) NOT NULL,
 mb_match_code varchar(15) NOT NULL,
 mb_2016_pid varchar(15) NOT NULL
);

INSERT INTO ADDRESS_MESH_BLOCK_2016 SELECT
  ogc_fid,address_mesh_block_2016_pid,date_created,date_retired,address_detail_pid, mb_match_code,mb_2016_pid 
FROM 
 ADDRESS_MESH_BLOCK_2016_SRC;

DROP TABLE IF EXISTS "ADDRESS_MESH_BLOCK_2016_SRC";

DROP TABLE IF EXISTS "ADDRESS_SITE_SRC";

CREATE TABLE "ADDRESS_SITE_SRC" AS
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
NSW_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM  
ACT_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
VIC_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
QLD_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
SA_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
QLD_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
NT_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
WA_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
TAS_ADDRESS_SITE_psv
UNION
SELECT ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
OT_ADDRESS_SITE_psv
;

DROP TABLE if exists "ACT_ADDRESS_SITE_psv";
DROP TABLE if exists "NSW_ADDRESS_SITE_psv";
DROP TABLE if exists "VIC_ADDRESS_SITE_psv";
DROP TABLE if exists "SA_ADDRESS_SITE_psv";
DROP TABLE if exists "QLD_ADDRESS_SITE_psv";
DROP TABLE if exists "NT_ADDRESS_SITE_psv";
DROP TABLE if exists "TAS_ADDRESS_SITE_psv"; 
DROP TABLE if exists "WA_ADDRESS_SITE_psv"; 
DROP TABLE if exists "OT_ADDRESS_SITE_psv"; 
DROP TABLE if exists "ADDRESS_SITE";

CREATE TABLE ADDRESS_SITE (
 ogc_fid integer,
 address_site_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_type varchar(8),
 address_site_name varchar(200)
);

INSERT INTO ADDRESS_SITE SELECT
  ogc_fid,address_site_pid,date_created,date_retired,address_type,address_site_name 
FROM 
 ADDRESS_SITE_SRC;

DROP TABLE IF EXISTS "ADDRESS_SITE_SRC";

DROP TABLE IF EXISTS "ADDRESS_SITE_GEOCODE_SRC";

CREATE TABLE "ADDRESS_SITE_GEOCODE_SRC" AS
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
NSW_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM  
ACT_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
VIC_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
QLD_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
SA_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM  
QLD_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
NT_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
WA_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
TAS_ADDRESS_SITE_GEOCODE_psv
UNION
SELECT ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
OT_ADDRESS_SITE_GEOCODE_psv
;

DROP TABLE if exists "ACT_ADDRESS_SITE_GEOCODE_psv";
DROP TABLE if exists "NSW_ADDRESS_SITE_GEOCODE_psv";
DROP TABLE if exists "VIC_ADDRESS_SITE_GEOCODE_psv";
DROP TABLE if exists "SA_ADDRESS_SITE_GEOCODE_psv";
DROP TABLE if exists "QLD_ADDRESS_SITE_GEOCODE_psv";
DROP TABLE if exists "NT_ADDRESS_SITE_GEOCODE_psv";
DROP TABLE if exists "TAS_ADDRESS_SITE_GEOCODE_psv"; 
DROP TABLE if exists "WA_ADDRESS_SITE_GEOCODE_psv"; 
DROP TABLE if exists "OT_ADDRESS_SITE_GEOCODE_psv"; 
DROP TABLE if exists "ADDRESS_SITE_GEOCODE";

CREATE TABLE ADDRESS_SITE_GEOCODE (
 ogc_fid integer,
 address_site_geocode_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 address_site_pid varchar(15),
 geocode_site_name varchar(200),
 geocode_site_description varchar(45),
 geocode_type_code varchar(4),
 reliability_code numeric(1) NOT NULL,
 boundary_extent numeric(7),
 planimetric_accuracy numeric(12),
 elevation numeric(7),
 longitude numeric(11,8),
 latitude numeric(10,8)
);

INSERT INTO ADDRESS_SITE_GEOCODE SELECT
  ogc_fid,address_site_geocode_pid,date_created,date_retired,address_site_pid,geocode_site_name,geocode_site_description,geocode_type_code, reliability_code, boundary_extent, planimetric_accuracy , elevation, longitude, latitude 
FROM 
 ADDRESS_SITE_GEOCODE_SRC;

DROP TABLE if exists "ADDRESS_SITE_GEOCODE_SRC";
 
DROP TABLE if exists "ADDRESS_TYPE_AUT";

CREATE TABLE ADDRESS_TYPE_AUT (
 ogc_fid integer,
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);

INSERT INTO ADDRESS_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_address_type_aut_psv;

DROP TABLE if exists "authority_code_address_type_aut_psv";

DROP TABLE if exists "ADDRESS_FLAT_TYPE_AUT";

CREATE TABLE ADDRESS_FLAT_TYPE_AUT (
 ogc_fid integer,
 code varchar(50) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(500)
);

INSERT INTO ADDRESS_FLAT_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_flat_type_aut_psv;

DROP TABLE if exists "authority_code_flat_type_aut_psv";
 
DROP TABLE if exists "GEOCODED_LEVEL_TYPE_AUT";

CREATE TABLE GEOCODED_LEVEL_TYPE_AUT (
 ogc_fid integer,
 code numeric(2) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(70)
);

INSERT INTO GEOCODED_LEVEL_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_geocoded_level_type_aut_psv;
 
DROP TABLE if exists "authority_code_geocoded_level_type_aut_psv";

DROP TABLE if exists "GEOCODE_RELIABILITY_AUT";

CREATE TABLE GEOCODE_RELIABILITY_AUT (
 ogc_fid integer,
 code numeric(1) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(100)
);

INSERT INTO GEOCODE_RELIABILITY_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_geocode_reliability_aut_psv;

DROP TABLE if exists "authority_code_geocode_reliability_aut_psv";

DROP TABLE if exists "GEOCODE_TYPE_AUT";

CREATE TABLE GEOCODE_TYPE_AUT (
 ogc_fid integer,
 code numeric(4) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(250)
);

INSERT INTO GEOCODE_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_geocode_type_aut_psv;

DROP TABLE if exists "authority_code_geocode_type_aut_psv";
 
DROP TABLE if exists "LEVEL_TYPE_AUT";

CREATE TABLE LEVEL_TYPE_AUT (
 ogc_fid integer,
 code varchar(4) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(30)
);

INSERT INTO LEVEL_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_level_type_aut_psv;
 
DROP TABLE IF EXISTS "authority_code_level_type_aut_psv";

DROP TABLE IF EXISTS "LOCALITY_SRC";

CREATE TABLE "LOCALITY_SRC" AS
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
NSW_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM  
ACT_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM  
VIC_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM  
QLD_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
SA_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM  
QLD_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
NT_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
WA_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
TAS_LOCALITY_PSV
UNION
SELECT ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
OT_LOCALITY_PSV
;

DROP TABLE if exists "ACT_LOCALITY_psv";
DROP TABLE if exists "NSW_LOCALITY_psv";
DROP TABLE if exists "VIC_LOCALITY_psv";
DROP TABLE if exists "SA_LOCALITY_psv";
DROP TABLE if exists "QLD_LOCALITY_psv";
DROP TABLE if exists "NT_LOCALITY_psv";
DROP TABLE if exists "TAS_LOCALITY_psv"; 
DROP TABLE if exists "WA_LOCALITY_psv"; 
DROP TABLE if exists "OT_LOCALITY_psv"; 
DROP TABLE if exists "LOCALITY";

CREATE TABLE LOCALITY (
 ogc_fid integer,
 locality_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_name varchar(100) NOT NULL,
 primary_postcode varchar(4),
 locality_class_code char(1) NOT NULL,
 state_pid varchar(15) NOT NULL,
 gnaf_locality_pid varchar(15),
 gnaf_reliability_code numeric(1) NOT NULL
);

INSERT INTO LOCALITY SELECT
  ogc_fid,locality_pid, date_created,date_retired,locality_name,primary_postcode,locality_class_code,state_pid,gnaf_locality_pid,gnaf_reliability_code
FROM 
 LOCALITY_SRC;
 
DROP TABLE if exists "LOCALITY_SRC";

DROP TABLE if exists "LOCALITY_ALIAS_TYPE_AUT";

CREATE TABLE LOCALITY_ALIAS_TYPE_AUT (
 ogc_fid integer,
 code varchar(10) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(100)
);

INSERT INTO LOCALITY_ALIAS_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_locality_alias_type_aut_psv;

DROP TABLE if exists "authority_code_locality_alias_type_aut_psv";

DROP TABLE if exists "LOCALITY_CLASS_AUT";

CREATE TABLE LOCALITY_CLASS_AUT (
 ogc_fid integer,
 code char(1) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(200)
);

INSERT INTO LOCALITY_CLASS_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_locality_class_aut_psv;
 
DROP TABLE IF EXISTS "authority_code_locality_class_aut_psv";

DROP TABLE IF EXISTS "LOCALITY_NEIGHBOUR_SRC";
 
CREATE TABLE "LOCALITY_NEIGHBOUR_SRC" AS
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
NSW_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM 
ACT_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM  
VIC_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM 
QLD_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
SA_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM 
QLD_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
NT_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
WA_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
TAS_LOCALITY_NEIGHBOUR_PSV
UNION
SELECT  ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
OT_LOCALITY_NEIGHBOUR_PSV
;

DROP TABLE if exists "ACT_LOCALITY_NEIGHBOUR_psv";
DROP TABLE if exists "NSW_LOCALITY_NEIGHBOUR_psv";
DROP TABLE if exists "VIC_LOCALITY_NEIGHBOUR_psv";
DROP TABLE if exists "SA_LOCALITY_NEIGHBOUR_psv";
DROP TABLE if exists "QLD_LOCALITY_NEIGHBOUR_psv";
DROP TABLE if exists "NT_LOCALITY_NEIGHBOUR_psv";
DROP TABLE if exists "TAS_LOCALITY_NEIGHBOUR_psv"; 
DROP TABLE if exists "WA_LOCALITY_NEIGHBOUR_psv"; 
DROP TABLE if exists "OT_LOCALITY_NEIGHBOUR_psv"; 
DROP TABLE if exists "LOCALITY_NEIGHBOUR";

CREATE TABLE LOCALITY_NEIGHBOUR (
 ogc_fid integer,
 locality_neighbour_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 neighbour_locality_pid varchar(15) NOT NULL
);

INSERT INTO LOCALITY_NEIGHBOUR  SELECT
 ogc_fid,locality_neighbour_pid,date_created,date_retired,locality_pid ,neighbour_locality_pid
FROM
 LOCALITY_NEIGHBOUR_SRC;

DROP TABLE if exists "LOCALITY_NEIGHBOUR_SRC";

DROP TABLE if exists "LOCALITY_POINT_SRC";

CREATE TABLE "LOCALITY_POINT_SRC" AS
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
NSW_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
ACT_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM  
VIC_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM 
QLD_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
SA_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
QLD_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
NT_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
WA_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
TAS_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
OT_LOCALITY_POINT_PSV
;

DROP TABLE if exists "ACT_LOCALITY_POINT_psv";
DROP TABLE if exists "NSW_LOCALITY_POINT_psv";
DROP TABLE if exists "VIC_LOCALITY_POINT_psv";
DROP TABLE if exists "SA_LOCALITY_POINT_psv";
DROP TABLE if exists "QLD_LOCALITY_POINT_psv";
DROP TABLE if exists "NT_LOCALITY_POINT_psv";
DROP TABLE if exists "TAS_LOCALITY_POINT_psv"; 
DROP TABLE if exists "WA_LOCALITY_POINT_psv"; 
DROP TABLE if exists "OT_LOCALITY_POINT_psv"; 
DROP TABLE if exists "LOCALITY_POINT";

CREATE TABLE LOCALITY_POINT (
 ogc_fid integer,
 locality_point_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 planimetric_accuracy numeric(12),
 longitude numeric(11,8),
 latitude numeric(10,8)
);

INSERT INTO LOCALITY_POINT  SELECT
 ogc_fid,locality_point_pid,date_created,date_retired,locality_pid,planimetric_accuracy,longitude,latitude
FROM
 LOCALITY_POINT_SRC;
 
DROP TABLE IF EXISTS "LOCALITY_POINT_SRC";

DROP TABLE IF EXISTS "MB_2011_SRC";

CREATE TABLE "MB_2011_SRC" AS
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
NSW_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
ACT_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM 
VIC_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
QLD_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
SA_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
QLD_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
NT_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
WA_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
TAS_MB_2011_PSV
UNION
SELECT ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
OT_MB_2011_PSV
;

DROP TABLE if exists "ACT_MB_2011_psv";
DROP TABLE if exists "NSW_MB_2011_psv";
DROP TABLE if exists "VIC_MB_2011_psv";
DROP TABLE if exists "SA_MB_2011_psv";
DROP TABLE if exists "QLD_MB_2011_psv";
DROP TABLE if exists "NT_MB_2011_psv";
DROP TABLE if exists "TAS_MB_2011_psv"; 
DROP TABLE if exists "WA_MB_2011_psv"; 
DROP TABLE if exists "OT_MB_2011_psv"; 
DROP TABLE if exists "MB_2011";

CREATE TABLE "MB_2011" (
 ogc_fid integer,
 mb_2011_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 mb_2011_code varchar(15) NOT NULL
);

INSERT INTO "MB_2011" SELECT
 ogc_fid,mb_2011_pid,date_created,date_retired,mb_2011_code
FROM
 MB_2011_SRC;
 
DROP TABLE IF EXISTS "MB_2011_SRC";

DROP TABLE IF EXISTS "MB_2016_SRC";
 
CREATE TABLE "MB_2016_SRC" AS
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
NSW_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
ACT_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM 
VIC_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
QLD_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
SA_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
QLD_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
NT_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
WA_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
TAS_MB_2016_PSV
UNION
SELECT ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
OT_MB_2016_PSV
;

DROP TABLE if exists "ACT_MB_2016_psv";
DROP TABLE if exists "NSW_MB_2016_psv";
DROP TABLE if exists "VIC_MB_2016_psv";
DROP TABLE if exists "SA_MB_2016_psv";
DROP TABLE if exists "QLD_MB_2016_psv";
DROP TABLE if exists "NT_MB_2016_psv";
DROP TABLE if exists "TAS_MB_2016_psv"; 
DROP TABLE if exists "WA_MB_2016_psv"; 
DROP TABLE if exists "OT_MB_2016_psv"; 
DROP TABLE if exists "MB_2016";

CREATE TABLE MB_2016 (
 ogc_fid integer,
 mb_2016_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 mb_2016_code varchar(15) NOT NULL
);

INSERT INTO MB_2016 SELECT
 ogc_fid,mb_2016_pid,date_created,date_retired,mb_2016_code
FROM
 MB_2016_SRC;

DROP TABLE if exists "MB_2016_SRC";

DROP TABLE if exists "MB_MATCH_CODE_AUT";

CREATE TABLE MB_MATCH_CODE_AUT (
 ogc_fid integer,
 code varchar(15) NOT NULL,
 name varchar(100) NOT NULL,
 description varchar(250)
);
 
INSERT INTO MB_MATCH_CODE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_mb_match_code_aut_psv;

DROP TABLE if exists "authority_code_mb_match_code_aut_psv";

DROP TABLE if exists "PS_JOIN_TYPE_AUT";

CREATE TABLE PS_JOIN_TYPE_AUT (
 ogc_fid integer,
 code numeric(2) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(500)
);
 
INSERT INTO PS_JOIN_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_ps_join_type_aut_psv;

DROP TABLE IF EXISTS "authority_code_ps_join_type_aut_psv";

DROP TABLE IF EXISTS "PRIMARY_SECONDARY_SRC";

CREATE TABLE "PRIMARY_SECONDARY_SRC" AS
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
NSW_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
ACT_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM 
VIC_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
QLD_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
SA_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
QLD_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
NT_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
WA_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
TAS_PRIMARY_SECONDARY_PSV
UNION
SELECT  ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
OT_PRIMARY_SECONDARY_PSV
;

DROP TABLE if exists "ACT_PRIMARY_SECONDARY_psv";
DROP TABLE if exists "NSW_PRIMARY_SECONDARY_psv";
DROP TABLE if exists "VIC_PRIMARY_SECONDARY_psv";
DROP TABLE if exists "SA_PRIMARY_SECONDARY_psv";
DROP TABLE if exists "QLD_PRIMARY_SECONDARY_psv";
DROP TABLE if exists "NT_PRIMARY_SECONDARY_psv";
DROP TABLE if exists "TAS_PRIMARY_SECONDARY_psv"; 
DROP TABLE if exists "WA_PRIMARY_SECONDARY_psv"; 
DROP TABLE if exists "OT_PRIMARY_SECONDARY_psv"; 
DROP TABLE if exists "PRIMARY_SECONDARY";

CREATE TABLE PRIMARY_SECONDARY (
 ogc_fid integer,
 primary_secondary_pid varchar(15) NOT NULL,
 primary_pid varchar(15) NOT NULL,
 secondary_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 ps_join_type_code numeric(2) NOT NULL,
 ps_join_comment varchar(500)
);
 
INSERT INTO PRIMARY_SECONDARY SELECT
 ogc_fid,primary_secondary_pid ,primary_pid,secondary_pid,date_created,date_retired,ps_join_type_code,ps_join_comment
FROM
 PRIMARY_SECONDARY_SRC;

DROP TABLE IF EXISTS "PRIMARY_SECONDARY_SRC";

DROP TABLE IF EXISTS "STATE_SRC";

CREATE TABLE "STATE_SRC" AS
SELECT  ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
NSW_STATE_PSV
UNION
SELECT  ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
ACT_STATE_PSV
UNION
SELECT  ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
VIC_STATE_PSV
UNION
SELECT  ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
QLD_STATE_PSV
UNION
SELECT ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
SA_STATE_PSV
UNION
SELECT ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
QLD_STATE_PSV
UNION
SELECT ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
NT_STATE_PSV
UNION
SELECT ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
WA_STATE_PSV
UNION
SELECT ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
TAS_STATE_PSV
UNION
SELECT ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
OT_STATE_PSV
;

DROP TABLE if exists "ACT_STATE_psv";
DROP TABLE if exists "NSW_STATE_psv";
DROP TABLE if exists "VIC_STATE_psv";
DROP TABLE if exists "SA_STATE_psv";
DROP TABLE if exists "QLD_STATE_psv";
DROP TABLE if exists "NT_STATE_psv";
DROP TABLE if exists "TAS_STATE_psv"; 
DROP TABLE if exists "WA_STATE_psv";
DROP TABLE if exists "OT_STATE_psv";
DROP TABLE if exists "STATE";

CREATE TABLE STATE (
 ogc_fid integer,
 state_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 state_name varchar(50) NOT NULL,
 state_abbreviation varchar(3) NOT NULL
);

INSERT INTO STATE SELECT
 ogc_fid,state_pid,date_created,date_retired,state_name,state_abbreviation
FROM
 STATE_SRC;

DROP TABLE if exists "STATE_SRC";

DROP TABLE if exists "STREET_CLASS_AUT";

CREATE TABLE STREET_CLASS_AUT (
 ogc_fid integer,
 code char(1) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(200)
);
 
INSERT INTO STREET_CLASS_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_street_class_aut_psv;

DROP TABLE if exists "authority_code_street_class_aut_psv";

DROP TABLE if exists "STREET_SUFFIX_AUT";

CREATE TABLE STREET_SUFFIX_AUT (
 ogc_fid integer,
 code varchar(15) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(30)
);
 
INSERT INTO STREET_SUFFIX_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_street_suffix_aut_psv;

DROP TABLE if exists "authority_code_street_suffix_aut_psv";

DROP TABLE if exists "STREET_TYPE_AUT";

CREATE TABLE STREET_TYPE_AUT (
 ogc_fid integer,
 code varchar(15) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(15)
);
 
INSERT INTO STREET_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_street_type_aut_psv;

DROP TABLE if exists "authority_code_street_type_aut_psv";
 
DROP TABLE if exists "STREET_LOCALITY_ALIAS_TYPE_AUT";

CREATE TABLE STREET_LOCALITY_ALIAS_TYPE_AUT (
 ogc_fid integer,
 code varchar(10) NOT NULL,
 name varchar(50) NOT NULL,
 description varchar(15)
);
 
INSERT INTO STREET_LOCALITY_ALIAS_TYPE_AUT  SELECT
 ogc_fid,code,name,description
FROM
 authority_code_street_locality_alias_type_aut_psv;

DROP TABLE IF EXISTS "authority_code_street_locality_alias_type_aut_psv";

DROP TABLE IF EXISTS "STREET_LOCALITY_SRC";

CREATE TABLE "STREET_LOCALITY_SRC" AS
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
NSW_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
ACT_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
VIC_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
QLD_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
SA_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
QLD_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
NT_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
WA_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
TAS_STREET_LOCALITY_PSV
UNION
SELECT ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
OT_STREET_LOCALITY_PSV
;

DROP TABLE if exists "ACT_STREET_LOCALITY_psv";
DROP TABLE if exists "NSW_STREET_LOCALITY_psv";
DROP TABLE if exists "VIC_STREET_LOCALITY_psv";
DROP TABLE if exists "SA_STREET_LOCALITY_psv";
DROP TABLE if exists "QLD_STREET_LOCALITY_psv";
DROP TABLE if exists "NT_STREET_LOCALITY_psv";
DROP TABLE if exists "TAS_STREET_LOCALITY_psv"; 
DROP TABLE if exists "WA_STREET_LOCALITY_psv";
DROP TABLE if exists "OT_STREET_LOCALITY_psv";
DROP TABLE if exists "STREET_LOCALITY";

CREATE TABLE STREET_LOCALITY (
 ogc_fid integer,
 street_locality_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 street_class_code char(1) NOT NULL,
 street_name varchar(100) NOT NULL,
 street_type_code varchar(15),
 street_suffix_code varchar(15),
 locality_pid varchar(15) NOT NULL,
 gnaf_street_pid varchar(15),
 gnaf_street_confidence numeric(1),
 gnaf_reliability_code numeric(1) NOT NULL
);
 
INSERT INTO STREET_LOCALITY  SELECT
 ogc_fid,street_locality_pid,date_created,date_retired,street_class_code,street_name,street_type_code,street_suffix_code ,locality_pid,gnaf_street_pid,gnaf_street_confidence,gnaf_reliability_code
FROM
 STREET_LOCALITY_SRC;

DROP TABLE IF EXISTS "STREET_LOCALITY_SRC";

DROP TABLE IF EXISTS "STREET_LOCALITY_ALIAS_SRC";

CREATE TABLE "STREET_LOCALITY_ALIAS_SRC" AS
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
NSW_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
ACT_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
VIC_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
QLD_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
SA_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
QLD_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
NT_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
WA_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT  ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
TAS_STREET_LOCALITY_ALIAS_PSV
UNION
SELECT  ogc_fid,street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
OT_STREET_LOCALITY_ALIAS_PSV
;

DROP TABLE if exists "ACT_STREET_LOCALITY_ALIAS_psv";
DROP TABLE if exists "NSW_STREET_LOCALITY_ALIAS_psv";
DROP TABLE if exists "VIC_STREET_LOCALITY_ALIAS_psv";
DROP TABLE if exists "SA_STREET_LOCALITY_ALIAS_psv";
DROP TABLE if exists "QLD_STREET_LOCALITY_ALIAS_psv";
DROP TABLE if exists "NT_STREET_LOCALITY_ALIAS_psv";
DROP TABLE if exists "TAS_STREET_LOCALITY_ALIAS_psv"; 
DROP TABLE if exists "WA_STREET_LOCALITY_ALIAS_psv"; 
DROP TABLE if exists "OT_STREET_LOCALITY_ALIAS_psv"; 
DROP TABLE if exists "STREET_LOCALITY_ALIAS";

CREATE TABLE STREET_LOCALITY_ALIAS (
 ogc_fid integer,
 street_locality_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 street_locality_pid varchar(15) NOT NULL,
 street_name varchar(100) NOT NULL,
 street_type_code varchar(15),
 street_suffix_code varchar(15),
 alias_type_code varchar(10) NOT NULL
);
 
INSERT INTO STREET_LOCALITY_ALIAS  SELECT
 ogc_fid, street_locality_alias_pid,date_created,date_retired,street_locality_pid,street_name,street_type_code,street_suffix_code,alias_type_code
FROM
 STREET_LOCALITY_ALIAS_SRC;

DROP TABLE IF EXISTS "LOCALITY_LOCAILITY_SRC";
 
CREATE TABLE "STREET_LOCALITY_POINT_SRC" AS
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
NSW_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
ACT_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
VIC_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
QLD_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
SA_STREET_LOCALITY_POINT_PSV
UNION
SELECT  ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
QLD_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
NT_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
WA_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
TAS_STREET_LOCALITY_POINT_PSV
UNION
SELECT ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
OT_STREET_LOCALITY_POINT_PSV
;

DROP TABLE if exists "ACT_STREET_LOCALITY_POINT_psv";
DROP TABLE if exists "NSW_STREET_LOCALITY_POINT_psv";
DROP TABLE if exists "VIC_STREET_LOCALITY_POINT_psv";
DROP TABLE if exists "SA_STREET_LOCALITY_POINT_psv";
DROP TABLE if exists "QLD_STREET_LOCALITY_POINT_psv";
DROP TABLE if exists "NT_STREET_LOCALITY_POINT_psv";
DROP TABLE if exists "TAS_STREET_LOCALITY_POINT_psv"; 
DROP TABLE if exists "WA_STREET_LOCALITY_POINT_psv"; 
DROP TABLE if exists "OT_STREET_LOCALITY_POINT_psv"; 
DROP TABLE if exists "STREET_LOCALITY_POINT";
CREATE TABLE STREET_LOCALITY_POINT (
 ogc_fid integer,
 street_locality_point_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 street_locality_pid varchar(15) NOT NULL,
 boundary_extent numeric(7),
 planimetric_accuracy numeric(12),
 longitude numeric(11,8),
 latitude numeric(10,8)
);
 
INSERT INTO STREET_LOCALITY_POINT  SELECT
 ogc_fid, street_locality_point_pid,date_created,date_retired,street_locality_pid,boundary_extent,planimetric_accuracy,longitude,latitude
FROM 
 STREET_LOCALITY_POINT_SRC;

DROP TABLE IF EXISTS "STREET_LOCALITY_POINT_SRC";

DROP TABLE IF EXISTS "LOCALITY_ALIAS_SRC";

CREATE TABLE "LOCALITY_ALIAS_SRC" AS
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
NSW_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
ACT_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
VIC_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM   
QLD_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
SA_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
QLD_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM 
NT_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM 
WA_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
TAS_LOCALITY_ALIAS_psv
UNION
SELECT ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM  
OT_LOCALITY_ALIAS_psv
;

DROP TABLE if exists "ACT_LOCALITY_ALIAS_psv";
DROP TABLE if exists "NSW_LOCALITY_ALIAS_psv";
DROP TABLE if exists "VIC_LOCALITY_ALIAS_psv";
DROP TABLE if exists "SA_LOCALITY_ALIAS_psv";
DROP TABLE if exists "QLD_LOCALITY_ALIAS_psv";
DROP TABLE if exists "NT_LOCALITY_ALIAS_psv";
DROP TABLE if exists "TAS_LOCALITY_ALIAS_psv"; 
DROP TABLE if exists "WA_LOCALITY_ALIAS_psv"; 
DROP TABLE if exists "OT_LOCALITY_ALIAS_psv"; 
DROP TABLE if exists "LOCALITY_ALIAS";

CREATE TABLE LOCALITY_ALIAS (
 ogc_fid integer,
 locality_alias_pid varchar(15) NOT NULL,
 date_created date NOT NULL,
 date_retired date,
 locality_pid varchar(15) NOT NULL,
 name varchar(100) NOT NULL,
 postcode varchar(4),
 alias_type_code varchar(10) NOT NULL,
 state_pid varchar(15) NOT NULL
);

INSERT INTO LOCALITY_ALIAS  SELECT
 ogc_fid,locality_alias_pid,date_created,date_retired,locality_pid,name,postcode,alias_type_code,state_pid
FROM 
 LOCALITY_ALIAS_SRC;

DROP TABLE if exists "LOCALITY_ALIAS_SRC";





