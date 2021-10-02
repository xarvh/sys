#!/bin/sh

#packages
apt-get --purge remove command-not-found thunderbird*
apt-get update
apt-get install $(cat packages)
apt-get upgrade

# Prevent power button from initiating shutdown
#echo HandlePowerKey=ignore >>/etc/systemd/logind.conf

#copy pmount.allow
#cp pmount.allow /etc/
cp sudoers.d/screen_brightness /etc/sudoers.d/

cp qtile/qtile.runner /usr/local/bin/
cp qtile/qtile.desktop /usr/share/xsessions/

cd
pip install xcffib
pip install --no-cache-dir cairocffi
pip install qtile


#cd automelee
#sudo -H ./root_setup.sh
