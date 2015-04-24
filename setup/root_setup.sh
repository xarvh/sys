
#packages
apt-get --purge remove command-not-found
apt-add-repository ppa:tycho-s/ppa
apt-get update
apt-get install $(cat packages)
apt-get upgrade

pip install udiskie

# Prevent power button from initiating shutdown
echo HandlePowerKey=ignore >>/etc/systemd/logind.conf

#copy pmount.allow
cp pmount.allow /etc/
