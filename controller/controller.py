import PyCmdMessenger
from celery import Celery

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

@app.task
def open_relay(id):
    """Open Relay <id>"""
    c.send("open_relay",int(id))

@app.task
def close_relay(id):
    """Close Relay <id>"""
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


