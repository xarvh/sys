#!/bin/sh

cd $HOME
rm -fr Music Pictures Public Templates Videos Documents
mkdir -p .usr


cd
DIR=.dati/sys
for i in $DIR/_*; do
  n=$(basename $i)
  t=.${n#_}
  rm -rf $t
  ln -fs $i $t 
done


#chmod -w -R $DIR/_fluxbox




