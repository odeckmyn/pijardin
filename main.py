#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from gpiozero import DigitalInputDevice

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

VALVE_STATES = ("closed","open","unknown")



class Valve(DigitalInputDevice):

    def __init__(cls, id):
        self.id = id
        self._state = "closed"
        self._gpioport = VALVES_MAPPING[self.id]
        super(self.__class__, self).__init__(self._gpioport)

    def __unicode__(self):
        return u"Valve #%d (GPIO %d), status=%s" % (self.id, self._gpioport, self._state)

    def open(self):
        self.on()

    def close(self):
        self.off()

class ValvesCollection(object):

    def __init__(cls, count=8):
        self.valves=[ Valve(id) for id in count(count) ]

valves=ValvesCollection()


