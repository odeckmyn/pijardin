import PyCmdMessenger, os.path
from celery import Celery
from datetime import datetime
from tinydb import TinyDB, Query

HERE = os.path.dirname(__file__)

# Log DB file
db = TinyDB(os.path.join(HERE,'..','controller-db.json'))

# Initialize an ArduinoBoard instance.  This is where you specify baud rate and
# serial timeout.  If you are using a non ATmega328 board, you might also need
# to set the data sizes (bytes for integers, longs, floats, and doubles).
arduino = PyCmdMessenger.ArduinoBoard("/dev/ttyUSB0", baud_rate=9600)

# List of command names (and formats for their associated arguments). These must
# be in the same order as in the sketch.
commands = [["open_relay","i"],
            ["close_relay","i"],

            ["get_relay_state","i"],
            ["return_relay_state","?"],

            ["ping",""],
            ["return_ping","s"],

            ["error","s"]]

# Initialize the messenger
c = PyCmdMessenger.CmdMessenger(arduino,commands)

# Initialize celery service
app = Celery('controller', broker='pyamqp://guest@localhost//')

RELAYS=(0,1,2,3,4,5,6,7,8)

@app.task
def open_relay(id):
    """Open Relay <id>"""
    c.send("open_relay",int(id))

@app.task
def close_relay(id):
    """Close Relay <id>"""
    c.send("close_relay",int(id))

@app.task
def close_relays():
    """Close all relays"""
    for id in RELAYS:
        c.send("close_relay",int(id))

@app.task
def get_relay_state(id):
    """Return state of Relay <id>.
    Returns True if opened, False if closed"""
    c.send("get_relay_state",int(id))
    msg = c.receive()
    return msg[1][0]

@app.task
def is_alive():
    """Returns True if arduino answers to ping"""
    c.send("ping")
    msg = c.receive()
    return msg[1][0]=='pong'

@app.task
def open_relay_for(id, duration):
    """Open Relay <id> for <duration> seconds"""
    open_relay(id)
    return close_relay_for.apply_async((id,), countdown=duration)

