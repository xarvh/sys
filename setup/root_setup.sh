
#packages
apt-get --purge remove command-not-found
apt-get update
apt-get install $(cat packages)
apt-get upgrade

#copy pmount.allow
cp $(HOME)/nw/instsys/pmount.allow /etc/
