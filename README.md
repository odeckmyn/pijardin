# Pi JARDIN

Simple automated irrigating system for your Pi

https://github.com/odeckmyn/pijardin

This software needs some cheap hardware (Pi, Arduino, relay board, spkinklers), and is built on top of free software (mostly Python 3.x)

## Requirements

- A Raspberry Pi (tested on a 2 B+)
- Any micro SD card
- An Arduino Nano board (ATmega328)
- Relay board

## Installation

### OS Installation

Download 'Raspbian Jessie Lite' from [official website](https://www.raspberrypi.org/downloads/raspbian/) and [burn](http://elinux.org/RPi_Easy_SD_Card_Setup) SD card.

Boot

    $ sudo raspi-config

- Adjust keyboard
- Activate SSH server

Then :

    $ sudo apt-get update
    $ sudo apt-get dist-upgrade

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

### Dependencies installation

Reach http://arduino.cc and install latest Arduino IDE (1.8.x today)

### Software installation

Connect to your Pi via SSH, using user `pi` :

    ssh pi@<myipaddress>

Stock password is `raspberry`. We strongly advice to change it and install and [ssh key](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2) for login.

#### Get the latest Pi Jardin

    $ cd ~
    $ sudo apt-get install git
    $ git clone https://github.com/odeckmyn/pijardin.git

#### Run installer

    $ cd pijardin
    $ make install

This will install all dependencies

#### Finalize

    $ source _venv3/bin/activate

## Updating my Pi Jardin

    $ cd
    $ cd pijardin
    $ source _venv/bin/activate
    $ make update

