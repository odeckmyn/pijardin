# Pi JARDIN

Simple automated irrigating system for your Pi

## Requirements

- A Raspberry Pi (tested on a 2 B+)
- Any micro SD card


## Installation

### OS Installation

Download 'Raspbian Jessie Lite' from [official website](https://www.raspberrypi.org/downloads/raspbian/) and burn SD card.

Boot

    $ sudo raspi-config

- Adjust keyboard
- Activate SSH server

Then :

    $ sudo apt-get update
    $ sudo apt-get upgrade

### Wifi Installation

    $ sudo vi /etc/wp /etc/wpa_supplicant/wpa_supplicant.conf

    country=FR
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
    ssid="<my wifi SSID>"
    psk="<my password>"
    }

And then :

    $ sudo reboot

### Software installation

#### Get the latest Pi Jardin

    $ sudo apt-get install git
    $ git clone https://github.com/odeckmyn/pijardin.git
    $ cd pijardin
    $ make install

#### Run installer

    $ make install

This will i

### Pi Jardin installation

Connect via SSH, using user `pi`

    $ git
