#!/bin/bash

for filename in ../G-NAF_unzipped_Feb_2019/G-NAF/G-NAF_FEBRUARY_2019/*.psv; do
    [ -e "$filename" ] || continue
    thetable=$(echo $filename| cut -d'/' -f 3)
    echo $thetable
    length=${#thetable}
    endindex=$(expr $length - 8)
    echo ${thetable:0:$endindex}
    var=${thetable:0:$endindex}
    echo $var
    echo $tablename
    sh dbcsvfun.sh   ${var}
done