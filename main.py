from time import sleep
from

VALVE_STATES = ("closed","open","unknown")

class Valve(object):

    def __init__(cls, id):
        self.id = id
        self._state = "closed"




