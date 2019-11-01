param([string]$rawaddrresses,[string]$cleanaddreses);
get-content rawaddresses.txt | % {$_.replace("/"," ")} |% {$_.replace("cres ","crescent ")} | % {$_.replace(","," ")} |% {$_.replace("st ","street ")} |% {$_.replace("  " , " ")} | out-file myaddresses.txt
