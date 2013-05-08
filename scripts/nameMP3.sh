#!/bin/sh
for i in $@
do
    id3v2 `nameMP3 $i -a -t` $i
    echo `nameMP3 $i -a -t` $i
#    echo -----------------------------------------------------------------
done
