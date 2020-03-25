library(dplyr)
library(csvread)
  
gnaf_df <- csvread("gnaf_feb_2020_address_view.csv",coltypes=c("string","string", "string","string",
                                                              "string","string", "string","string",
                                                              "string","string", "string","string",
                                                              "string","string", "integer","string",
                                                              "string","string", "string","string",
                                                              "integer","string",  "double","double",
                                                              "string"),header = TRUE)
gnaf_df[,'AddressText']=trimws(gnaf_df[,'AddressText'])
search_df <- read.csv("addresses_cleaned.txt",sep=",", stringsAsFactors=FALSE)
  
  
find_address <- function(searchText,gnaf_df,id=1) {
  search_result <- dplyr::filter(gnaf_df, grepl(searchText, AddressText))
  result <- data.frame(c(id,searchText,search_result[1,]))
  colnames(result)[1] <- "id"
  colnames(result)[2] <- "searchText"
  return(result)
}
  
batch_search <- function (search_df,gnaf_df) {
  results_df <- data.frame(id="", searchText="", Address_Detail_PID="", Street_Locality_PID="",
                           Locality_PID="", Building_Name="", Lot_Number_Prefix="", Lot_Number="",
                           Lot_Number_Suffix="", Flat_Type="", Flat_Number_Prefix="", Flat_Number="",
                           Flat_Number_Suffix="", Level_Type="", Level_Number="", Number_First_Prefix="",
                           Number_First="", Street_Name="", Street_Type_Code="", Locality_Name="",
                           State_Abbreviation="", Postcode="", Confidence="", AddressText="",
                           Latitude="", Longitude="", Geocode_Type.="", stringsAsFactors=FALSE)
  for (i in 1:nrow(search_df)) 
  {
    print(paste("processing address",i))
    search <- find_address(search_df[i,1],gnaf_df,i)
  
    results_df <- rbind(results_df,search)
  
  }
  return(results_df[-1,])
}
  
processed <- batch_search(search_df,gnaf_df)
write.csv(processed,"addresses_processed.csv", row.names=FALSE, quote=FALSE)

