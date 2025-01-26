#!/bin/sh

# TODO find a better way to get the path
cd $(dirname $0)
cd ..
DIR=`pwd`

cd
rm -fr Music Pictures Public Templates Videos Documents
mkdir -p .usr
mkdir -p .vim/tmp

cd
cd .config
ln -s ../.usr/sys/qtile .
ln -s ../.usr/sys/mc .

cd
for i in $DIR/_*; do
  n=$(basename $i)
  t=.${n#_}
  rm -rf $t
  ln -fs $i $t 
done
