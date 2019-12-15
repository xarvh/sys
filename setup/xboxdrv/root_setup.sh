cd
curl -O https://gist.githubusercontent.com/xarvh/6abfbd176a48e21886813e98480e9dc5/raw/96642aeea1a1f59d9f59cff5b6ecbb20362fdfd3/xboxdrv.service
sudo apt install xboxdrv
sudo mv xboxdrv.service /etc/systemd/system
sudo systemctl enable xboxdrv
sudo systemctl start xboxdrv
