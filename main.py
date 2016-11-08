#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from gpiozero import DigitalOutputDevice

VALVES_MAPPING = {
    # valve ID : GPIO Port,
    1 : 19,
    2 : 13,
    3 : 6,
    4 : 5,
    5 : 5,22,
    6 : 27,
    7 : 17,
    8 : 4,
}
VALVES_COUNT = len(VALVES_MAPPING.keys())

class Valve(DigitalOutputDevice):

    def __init__(self, id):
        self.id = id
        self._state = "closed"
        self._gpioport = VALVES_MAPPING[self.id]
        super(self.__class__, self).__init__(self._gpioport, active_high=False)

    def water(self):
        self.on()

    def nowater(self):
        self.off()

class ValvesCollection(object):

    def __init__(self, count=VALVES_COUNT):
        self.valves=[ Valve(id+1) for id in range(count) ]

    def __getitem__(self, id):
        return self.valves[id-1]


valves=ValvesCollection()


