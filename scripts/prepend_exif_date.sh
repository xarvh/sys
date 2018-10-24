for i in s* ;do  mv $i "$(exiftool -T -createdate $i)$i"; done
