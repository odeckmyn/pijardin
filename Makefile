# ARDUINO_INSTALL_DIR=~/Downloads/arduino-1.8.3/
# ARDUINO_PORT=/dev/ttyUSB0
# ARDUINO_BAUD=57600
# ARDUINO_ARCHITECTURE=avr
# ARDUINO_BOARD_TAG=atmega328
# ARDUINO_BOARD_TAG=atmegang
# ARDUINO_BOARD_SUB=atmega328

include /usr/share/arduino/Arduino.mk

default:
	@echo "Nothing to do by default. Please read the manual."

# -- Python Virtual Env machinery --------------------
virtualenv.installed: _venv3/bin/activate

_venv3/bin/activate: requirements.txt
	test -d _venv3 || virtualenv -p /usr/bin/python3 _venv3
	_venv3/bin/pip install -Ur requirements.txt
	touch _venv3/bin/activate

virtualenv:
	@if test "$(VIRTUAL_ENV)" = "" ; then \
		echo "**** Please first start your virtualenv : source _venv3/bin/activate ****"; \
		echo "* First install : make virtualenv.installed"
		exit 1; \
	fi

# -- Install section --------------------

install: install.pkg install.python install.arduino

install.pkg:
	sudo apt-get update
	sudo apt-get install ipython python-pip
	sudo apt-get install rabbitmq-server

install.python: virtualenv.installed

install.arduino: install.pkg
	sudo apt-get install arduino-mk

# -- Arduino section -------------------

arduino.build:

arduino.upload:


# -- Update section --------------------

update: virtualenv update.git

update.git:
	git pull

# -- Dev section --------------------
dev.test: virtualenv
	python test_main.py
