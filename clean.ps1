get-content addresses_raw.txt |
% {$_.ToUpper()} |
% {$_.replace("`t","")} |
% {$_.replace("\s+"," ")} |
% {$_.replace("/"," ")} |
% {$_.replace(","," ")} |
% {$-.replace('"','')} |
% {$_.replace(" LOOP "," LOOP ")}|
% {$_.replace(" RISE "," RISE ")}|
% {$_.replace(" ARC "," ARCADE ")}|
% {$_.replace(" ESP "," ESPLANADE ")}|
% {$_.replace(" CV "," COVE ")}|
% {$_.replace(" CRES "," CRESCENT ")}|
% {$_.replace(" CR "," CRESCENT ")}|
% {$_.replace(" ST "," STREET ")}|
% {$_.replace(" RD "," ROAD ")}|
% {$_.replace(" AVE "," AVENUE ")}|
% {$_.replace(" PL "," PLACE ")}|
% {$_.replace(" CRT "," COURT ")}|
% {$_.replace(" CT "," COURT ")}|
% {$_.replace(" DR "," DRIVE ")}|
% {$_.replace(" TCE "," TERRACE ")}|
% {$_.replace(" PDE "," PARADE ")}|
% {$_.replace(" CCT "," CIRCUIT ")}|
% {$_.replace(" CRST "," CREST ")}|
% {$_.replace(" LA "," LANE ")}|
% {$_.replace(" WAY "," WAY ")}|
% {$_.replace(" GDN "," GARDENS ")}|
% {$_.replace(" GDNS "," GARDENS ")}|
% {$_.replace(" CL "," CLOSE ")}|
% {$_.replace(" HWY "," HIGHWAY ")}|
% {$_.replace(" CCS "," CIRCUS ")}|
% {$_.replace(" CCL "," CIRCLE ")}|
% {$_.replace(" BVD "," BOULEVARD ")}|
% {$_.replace(" BLVD "," BOULEVARD ")}|
% {$_.replace(" ST "," STREET ")}|
% {$_.replace(" MT "," MOUNT ")}|
% {$_.replace(" STREET KILDA "," ST KILDA ")}|
% {$_.replace(" RD "," ROAD ")}|
% {$_.replace(" HWY "," HIGHWAY ")}|
% {$_.replace("  " , " ")} | 
out-file addresses_cleaned.txt
