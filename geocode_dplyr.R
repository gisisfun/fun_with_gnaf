library(dplyr)
library(stringr) 
library(readr)

col_list = list(col_character(),col_character(),col_character(),col_character(),col_character(),col_character(),col_character(),
                col_character(),col_character(),col_character(),col_character(),col_character(),col_character(),col_character(),
                col_integer(),col_character(),col_character(),col_character(),col_character(),col_character(),col_integer(),
                col_character(),col_double(),col_double(),col_character())

gnaf_df <- read_csv("gnaf_feb_2020_address_view.csv", col_types = col_list)
str(gnaf_df)

search_df <- read.csv("addresses_cleaned.txt",sep=",", stringsAsFactors=FALSE)
  
  
find_address <- function(searchText,gnaf_df,id=1) {
  search_result <- gnaf_df  %>% 
    filter(str_detect(AddressText,searchText))
  result <- data.frame(c(id,searchText,data.frame(search_result)))
  colnames(result)[1] <- "id"
  colnames(result)[2] <- "searchText"
  return(result)
}
  
batch_search <- function (search_df,gnaf_df) {
  results_df <- data.frame(id=NaN, searchText=NA, Address_Detail_PID=NA, Street_Locality_PID=NA,
                           Locality_PID=NA, Building_Name=NA, Lot_Number_Prefix=NA, Lot_Number=NA,
                           Lot_Number_Suffix=NA, Flat_Type=NA, Flat_Number_Prefix=NA, Flat_Number=NA,
                           Flat_Number_Suffix=NA, Level_Type=NA, Level_Number=NA, Number_First_Prefix=NA,
                           Number_First=NA, Street_Name=NA, Street_Type_Code="", Locality_Name=NA,
                           State_Abbreviation=NA, Postcode="", Confidence=NaN, AddressText=NA,
                           Latitude=NaN, Longitude=NaN, Geocode_Type=NA, stringsAsFactors=FALSE)
  for (i in 1:nrow(search_df)) 
  {
    print(paste("processing address",i))
    search <- find_address(search_df[i,1],gnaf_df,i)
    results_df <- rbind(results_df,search)
  }
  return(results_df[-1,])
}
  
process_df <- batch_search(search_df,gnaf_df)
write.csv(process_df,"addresses_processed.csv", row.names=FALSE, quote=FALSE)

#names(gnaf_df)
#?read_csv