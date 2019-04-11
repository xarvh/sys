#!/bin/sh
pip install keyboard
cp automelee.service /etc/systemd/system
cp automelee /usr/local/bin
systemctl enable automelee
systemctl start automelee
