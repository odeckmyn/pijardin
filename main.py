from time import sleep

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



class Valve(object):

    def __init__(cls, id):
        self.id = id
        self._state = "closed"
        self._gpioport = VALVES_MAPPING[self.id]

    def __unicode__(self):
        return u"Valve #%d (GPIO %d), status=%s" % (self.id, self._gpioport, self._state)

    def open(self):
        pass

    def close(self):
        pass

class ValvesCollection(object):

    def __init__(cls, count=8):
        self.valves=[ Valve(id) for id in count(count) ]

valves=ValvesCollection()






