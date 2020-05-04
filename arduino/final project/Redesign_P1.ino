/* INITIALIZATION
   ============== */

// relevant libraries and constants
#include <SevSeg.h>
#include <Servo.h>
#define buttonPin 11
#define tempPin A0
#define servoPin 12

// relevant variables
int buttonState; int lastState;
float vOut; float temp;
int mode = 0;
int servoPos = 30;

// initialize the 7-segment and the servo
SevSeg displ;
Servo serv;

/* SETUP
   ==== */

void setup() {
  // display setup
  byte numDigits = 1;
  byte digitPins[] ={};
  byte segmentPins[] = { 2, 3, 4, 5, 6, 7, 8, 9 };
  bool resistorsOnSegments = true;
  byte hardwareConfig = COMMON_ANODE;
  displ.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
  displ.setBrightness(90);
  displ.setNumber('-');
  displ.refreshDisplay();
  
  // button setup
  pinMode(buttonPin,INPUT);
  
  // servo setup
  serv.attach(servoPin);
  serv.write(30);
  
  // temperature sensor setup
  analogReference(DEFAULT);

  // Serial monitor initialization
  Serial.begin(9600);
  Serial.println("Welcome to the temperature display program.");
  Serial.println("This program will display the current temperature");
  Serial.println("both on the Serial Monitor and on the attached");
  Serial.println("7-segment display.");
  Serial.println("The default units are Celsius.");
  displayUsage();
}

/* MAIN PROGRAM AND FUNCTIONS
   ========================== */
   
void loop() {
  /* this section of code gets input from the serial monitor
     to determine what the units should be for the next
     temperature reading */
  if (Serial.available()){
    char ch = Serial.read();
    int cha = (int) ch;
    if (ch == 'f' || ch == 'F'){
      mode = 1;
      servoPos = 120;
      serv.write(servoPos);
      Serial.print("\n<MESSAGE>  ");
      Serial.println("You have successfully changed the output units to Fahrenheit.\n");
    } else if (ch == 'c' || ch == 'C'){
      mode = 0;
      servoPos = 30;
      serv.write(servoPos);
      Serial.print("\n<MESSAGE>  ");
      Serial.println("You have successfully changed the output units to Celsius.\n");
    } else if (cha == 10 || cha == 13) { ; }// ignores the newline char
    else if (ch == 'h' || ch == 'H'){
      displayUsage();
    } else {
      Serial.print("\n<MESSAGE>  ");
      Serial.print("Input not recognized: ");
      Serial.print(ch);
      Serial.println(" Please try again.\n"); 
    }
  }

  /* this block of code will alter what is actually seen in 
     the arduino components - the servo pointer, and the 
     7-segment display */
  buttonState = digitalRead(buttonPin);
  int a = analogRead(tempPin);
  vOut = (a/1024.0)*5000;
  temp = (vOut - 500)/10;
  if (buttonState == HIGH && buttonState != lastState){
    if (mode == 0){
      Serial.print("The current temperature is: ");
      Serial.print(temp);
      Serial.println(" ºC");
      displayTemp(temp);
    }
    else {
      temp = temp*(9/5.0) + 32;
      Serial.print("The current temperature is: ");
      Serial.print(temp);
      Serial.println(" ºF");
      displayTemp(temp);
    }
  }
  lastState = buttonState;
  displ.refreshDisplay();
  delay(150);
} // end of loop

// this function displays the temp on the 7-segment display
void displayTemp(float t){
  // calculating each digit of the temp
  int intPart = (int) t;
  int floatPart = ((t - intPart) * 100) + 1;
  int pl10 = intPart / 10;
  int pl1 = intPart % 10;
  int pl1th = floatPart / 10;
  int pl10th = floatPart % 10;
  // displaying each digit for 1.5 seconds
  displ.setNumber(pl10);
  displ.refreshDisplay();
  delay(1500);
  displ.setNumber(pl1,0);
  displ.refreshDisplay();
  delay(1500);
  displ.setNumber(pl1th);
  displ.refreshDisplay();
  delay(1500);
  displ.setNumber(pl10th);
  displ.refreshDisplay();
  delay(1500);
  displ.setNumber('-');
}

void displayUsage(){
  Serial.println("  Usage:");
  Serial.println("    F or f       -  change units to Fahrenheit");
  Serial.println("    C or c       -  change units to Celsius");
  Serial.println("    Push button  -  display temperature");
  Serial.println("    H or h       -  see this menu again");
  }
