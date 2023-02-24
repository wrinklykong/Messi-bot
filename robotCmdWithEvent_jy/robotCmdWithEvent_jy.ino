/*
  Serial Event example
 
 When new serial data arrives, this sketch adds it to a String.
 When a newline is received, the loop prints the string and 
 clears it.
 
 A good test for this is to try it with a GPS receiver 
 that sends out NMEA 0183 sentences. 
 
 Created 9 May 2011
 by Tom Igoe
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/SerialEvent
 
 */
 
#include <Wire.h>                // include the PRIZM library in the sketch
#include <PRIZM.h>               // include the PRIZM library in the sketch
PRIZM prizm;                     // instantiate a PRIZM object “prizm” so we can use its functions

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
String outputString = "";        // a string to hold outgoing data

int cmd = 0;                     // an integer to store the cmd
int para = 0;                    // an integer to store the parameter
String cmdStr = "";              // a string to store the cmd
String paraStr = "";             // a string to store the parameter

void setup() {
  prizm.PrizmBegin();            // start prizm
  
  prizm.setMotorInvert(1,1);     // invert the direction of DC Motor 1
                                 // to harmonize the direction of opposite facing drive motors
                                 
  Serial.begin(9600);            // initialize serial:
  
  // reserve 20/10 bytes for the string:
  inputString.reserve(20);
  outputString.reserve(20);
  cmdStr.reserve(10);
  paraStr.reserve(10);
}

void loop() {
  // when stringComplete is true, we take actions
  if (stringComplete) {
    cmdStr = inputString.substring(0,1);   // first byte is cmd
    paraStr = inputString.substring(1);    // remaining is the parameter
    
    cmd = cmdStr.toInt();                  // convert string cmd to integer cmd
    para = paraStr.toInt();                // convert string parameter to integer parameter
    
    switch (cmd) {
      case 1:{
        // ??
        break;
      }
      case 2:{
        // Turn left
        prizm.setMotorPowers(-para,para);
        break;
      }
      case 3:{
        // Turn right
        prizm.setMotorPowers(para,-para);
        break;
      }
      case 4:{
        // Move forward
        prizm.setMotorPowers(para,para);
        break;
      }
      case 5:{
        // Move backwards
        prizm.setMotorPowers(-para,-para);
        break;
      }
      // kick
      case 6:{
        prizm.setMotorPowers(100,125);
        break;
      }
      // stop motor
      case 7:{
        prizm.setMotorPowers(0,0);
        break;
      }
      // brake motor
      case 8:{
        prizm.setMotorPowers(125,125);
        break;
      }
      // skrrt
      case 9:{
        prizm.setMotorPowers(-10,15);
        break;
      }
    }
    
    // here we dont directly send the inputString
    // because we need to show we decode the cmd and parameter correctly
    outputString += cmdStr;
    outputString += String(para);          // use para instead of paraStr to avoid duplicated '\n'
    Serial.println(outputString);          // println helps us to send back msg with a '\n' at the end
    
    // clear the variables
    inputString = "";
    outputString = "";
    cmdStr = "";
    paraStr = "";
    cmd = 0;
    para = 0;
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}


