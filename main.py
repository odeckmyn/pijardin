#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from gpiozero import DigitalOutputDevice

VALVES_MAPPING = {
    # valve ID : GPIO Port,
    1 : 4,
    2 : 17,
    3 : 27,
    4 : 22,
    5 : 5,
    6 : 6,
    7 : 13,
    8 : 19,
}
VALVES_COUNT = len(VALVES_MAPPING.keys())

VALVE_STATES = ("closed","open","unknown")


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
        return self.valves[id]


valves=ValvesCollection()


