// ********  PiJardin Arduino Software **********
// (c) Olivier Deckmyn 2017
// Licence : GPL3

// This software is reponsible for receiving commands via USB Serial and activate
// the relay opening/closing water in the garden, along with counting and storing
// flow sensor data

#include "CmdMessenger.h"

// === PARAMETERS ===================
// customize the app by modifying these values :

const int relayPins[] = {10, 9, 8, 7, 6, 5, 4, 3}; // Pins for the relays, ordered
const int flowSensorPin = 2;  // Pin of Flow Sensor (has to be 2 or 3)
const long BAUD_RATE = 9600;

// ==== GLOBAL VARIABLES ========================

CmdMessenger c = CmdMessenger(Serial,',',';','/');
const int relaysCount = sizeof(relayPins)/sizeof(int); // Number of relays attached to the arduino

// ==== RELAY OBJECT ============================
enum relayState { closed, opened };

struct Relay{
  int pin; // Relay pin number
  relayState state; // Relay state
};

Relay* relays[relaysCount]; // an array of all know relays

// -- RELAY METHODS ---------------------
void openRelay(Relay* r){
  digitalWrite( r->pin, LOW );
  r->state = opened;
}

void closeRelay(Relay* r){
  digitalWrite( r->pin, HIGH );
  r->state = closed;
}

bool readRelayState(Relay* r){
  return(digitalRead(r->pin));
  //return(r->state);
}


// ==== CmdMessenger METHODS =========================

/* Define available CmdMessenger commands */
/* Make sure these functions are implemented AND declared in _attach_callbacks */
enum {
    open_relay,
    close_relay,
    
    get_relay_state,
    return_relay_state,

    ping,
    return_ping,
    
    error,
};

// ---- callbackd -----------------------------------
void on_open_relay(void){
    int id = c.readBinArg<int>();
    openRelay(relays[id]);
}

void on_ping(void){
    c.sendCmd(return_ping, "pong");
}

void on_close_relay(void){
    int id = c.readBinArg<int>();
    closeRelay(relays[id]);
}

void on_get_relay_state(void){
    int id = c.readBinArg<int>();
  
    /* Send result back */
    c.sendBinCmd(return_relay_state, (bool)relays[id]->state  );
}

void on_unknown_command(void){
    c.sendCmd(error,"Unknown command");
}


void _attach_callbacks(void) {

    c.attach(open_relay, on_open_relay);
    c.attach(close_relay, on_close_relay);
    c.attach(get_relay_state, on_get_relay_state);
    c.attach(ping, on_ping);
    c.attach(on_unknown_command);
}


// ==== GENERAL METHODS =========================

// Initialise the arduino pins and the internal machinery
void _init_pins() {
  for (int i=0; i<relaysCount; i++) {
    int pin = relayPins[i];
    // Initialise the Arduino data pins for OUTPUT
    pinMode(pin, OUTPUT);
    
    Relay *r = new Relay; // make a new Relay object
    relays[i] = r; // store it in the array
    
    // and now initialize it
    r->pin=pin;
    closeRelay(r);
    
  }
}

// A method testing opening each Relay for the given DELAY milliseconds.
void roller_coaster(int DELAY=500) {
  for (int i=0; i<relaysCount; i++) {
    Relay* relay = relays[i];
    openRelay(relay);
    delay(DELAY);
    closeRelay(relay);
  }
}

// ********************* ARDUINO SETUP FUNCTION ************************

void setup() {
  _init_pins();
//  rtc.begin()
  
  Serial.begin(BAUD_RATE);
  c.printLfCr();
  _attach_callbacks();
  
  roller_coaster(50);
}

// ********************* ARDUINO MAIN LOOP ************************

void loop() {
  c.feedinSerialData();
}
