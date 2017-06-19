import PyCmdMessenger
import os.path, logging
from celery import Celery
from datetime import datetime
from tinydb import TinyDB, Query

HERE = os.path.dirname(__file__)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
  datefmt="%m-%d %H:%M", filename=os.path.join(HERE,'..', 'controller.log'), filemode="w")
console=logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logging.getLogger('').addHandler(console)


# Log DB file
db = TinyDB(os.path.join(HERE,'..','controller-db.json'))

# List of command names (and formats for their associated arguments). These must
# be in the same order as in the sketch.
commands = [["open_relay","i"],
            ["close_relay","i"],

            ["get_relay_state","i"],
            ["return_relay_state","?"],

            ["ping",""],
            ["return_ping","s"],

            ["error","s"]]


# Initialize an ArduinoBoard instance.  This is where you specify baud rate and
# serial timeout.  If you are using a non ATmega328 board, you might also need
# to set the data sizes (bytes for integers, longs, floats, and doubles).
arduino = PyCmdMessenger.ArduinoBoard("/dev/ttyUSB0", baud_rate=9600)

# Initialize the messenger
c = PyCmdMessenger.CmdMessenger(arduino,commands)

# Initialize celery service
app = Celery('controller', broker='pyamqp://guest@localhost//')

RELAYS=(0,1,2,3,4,5,6,7)

@app.task
def open_relay(id):
    """Open Relay <id>"""
    logging.info("open relay %d"%id)
    c.send("open_relay",int(id))

@app.task
def close_relay(id):
    """Close Relay <id>"""
    logging.info("close relay %d"%id)
    c.send("close_relay",int(id))

@app.task
def close_relays():
    """Close all relays"""
    logging.info("close all relays")
    for id in RELAYS:
        close_relay(id)

@app.task
def get_relay_state(id):
    """Return state of Relay <id>.
    Returns True if opened, False if closed"""
    c.send("get_relay_state",int(id))
    msg = c.receive()
    result=msg[1][0]
    logging.info("relay %d state : %s"%(id, result))
    return result

@app.task
def get_relay_states():
    """Return state of all relays.
    Returns a list of [True if opened, False if closed]"""
    result=[]
    for id in RELAYS:
        result.append( get_relay_state(id) )
    logging.info("relays states : %s"%result)
    return result

@app.task
def is_alive():
    """Returns True if arduino answers to ping"""
    c.send("ping")
    msg = c.receive()
    result=msg[1][0]=='pong'
    logging.info("ping : %s"%result)
    return result

@app.task
def open_relay_for(id, duration):
    """Open Relay <id> for <duration> seconds"""
    logging.info("open relay %d for %d s"%(id, duration))
    open_relay(id)
    return close_relay.apply_async((id,), countdown=duration)

