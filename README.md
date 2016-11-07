# Pi JARDIN

Simple automated irrigating system for your Pi

## Installation

Raspberry Pi 2 B+
MicroSD 16Go


### OS Installation

Raspbian Jessie Lite

Boot

$ sudo raspi-config
-> keyboard
-> SSH

$ sudo apt-get update && sudo apt-get upgrade

### Installation Wifi

$ sudo vi /etc/wp /etc/wpa_supplicant/wpa_supplicant.conf

country=FR
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid="<my wifi SSID>"
psk="<my password>"
}


$ sudo reboot

### Python Installation

$ sudo apt-get install ipython python-pip
$ sudo pip install gpiozero

