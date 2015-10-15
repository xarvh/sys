#!/bin/sh
#
# --new		use only Musica/new/good/
# --sort	use only Musica/new/unsorted
#
# otherwise adds all categories and all Musica/new/good/
#

#
# base paths
#
OUT="$HOME/.playlist"
DIR="$HOME/Musica"

#
# secondary directories
#
CAT="$DIR/categories"
NEW="$DIR/new/good"
SORT="$DIR/new/unsorted"

#
# internal stuff
#
PLAYDIRS="$CAT $NEW"
NOPLAY=""
GREPS=""
TMP="/tmp/playlist.$USER.tmp"



#
# process all arguments
#
for a in $@; do
    if [ "$a" = "--sort" ]; then
	# pick ONLY the tracks not yet sorted out
	PLAYDIRS=$SORT
    elif [ "$a" = "--new" ]; then
        # pick ONLY the tracks that have been just sorted out
	PLAYDIRS=$NEW
    elif [ "$a" = "--noplay" ]; then
        # pick ONLY the tracks that have been just sorted out
	NOPLAY="true"
    else
	GREPS="$GREPS $a"
    fi
done



#
# build file list
#
rm -f $TMP
for d in $PLAYDIRS; do
    find $d/* 2>/dev/null |grep -v "pacco" >>$TMP
done

#
# filter tracks
#
for g in $GREPS; do
    grep -i $g $TMP >$TMP.grep
    mv $TMP.grep $TMP
done



#
# filter out directories, shuffle, and write output
#
egrep -i '(mp3|ogg)$' $TMP |shuf -o $OUT



#
# play!
#
if [ "$NOPLAY" = "" ]; then
    playlist.player $OUT 2>/dev/null
fi
