//EE302 Term Project Arduino code
//Written by Barkın Tuncer (tuncer.barkin@gmail.com)
//Please send an email if you have any suggestions or find any bugs
//All rights are reserved

#define motorOutputPin 9

// Likely User Modified Variables ******************************
unsigned long deltaT = 1000; // time between samples (usecs) 1000->50000
const int pastSize = 3; // used for integrating

//These two values have to be set according to your setup
float angle_multip = 0.2; // Multiplies the analog read value that is coming from the POT
float angle_base = 90; // The bias term to adjust the angle accordingly

float duration = 0; // The duration between two loops
// double p_time = 0; // A variable to hold past time
unsigned long p_time = 0; // A variable to hold past time
// End Likely User Modified Variables***************************

int angleSensorPin = A0; // Arduino Analog 0 pin should be connected to POT's middle leg.
int pwmVoltagePin = A1;
int motorVoltagePin = A2;
float pastError[pastSize]; //Holds the past errors
// float sum; //sum initialized edilmesi gerekiyo bence
float sum; //Holds the summation of the errors

int dacMax = 255; // Arduino dac is eight bits.
int adcMax = 1024; //Arduino uses a 10 bit dac, 10th power of 2 = 1024
int adcCenter = 512; // 1024/2

float direct = 0; // Direct motor command from host.
float desired = 0; // Desired value (speed or angle) from host.
float Kp = 0; // Feedback gains (proportional)
float Kd = 0; // Feedback gains (delta)
int enable_pwm = 1;
float Ki = 0; // Feedback gains (sum)
float maxSum = 1; // Optional integral term

unsigned long delta; //Calculates the derivative of the error


unsigned long t; //time variable
int incoming[7]; // array that holds the variabels coming from GUI
char pos_neg; // defines being positive or negative for "Desired"

void setup() {
  // Pin initialization
  pinMode(motorOutputPin, OUTPUT);
  pinMode(motorVoltagePin, INPUT);
  pinMode(pwmVoltagePin, INPUT);
  Serial.begin(19200);
}


void loop() {
  t = millis();
  duration = t - p_time;
  p_time = t;
  // Reads the data coming from the GUI.
  if (Serial.available() >= 7) {
    for (int i = 0; i < 7; i++) {
      incoming[i] = Serial.read();
    }
  }
  //Assignment of each variable.
  Kp = incoming[0] / 10.0; // Feedback gains (proportional)	# for example if you want 1.5, you make Kp slider 15
  Kd = incoming[1] / 10.0; // Feedback gains (delta)
  Ki = incoming[2] / 10.0; // Feedback gains (sum)
  desired = incoming[3] / 10.0; // Desired height
  direct = incoming[4] / 10.0; // Direct is the desired value for part 1 ???
  maxSum = incoming[5] / 10.0; // Optional integral term
  enable_pwm = incoming[6];
  // User modifiable code between stars!!
  /***********************************************/
  // Measure angle three times and sum, then by twelve. Averaging reduces noise.
  // Factor of four is ratio of adc and dac.
  //float ang = float (analogRead(angleSensorPin)+ analogRead(angleSensorPin) + analogRead(angleSensorPin) - 3*adcCenter)/12.0;
  //A simpler code to calculate angle. Useless in part 1.
/*
  float ang = float (analogRead(angleSensorPin) * angle_multip) - angle_base;

  //Measuring and calculating motor speed.
  int VmotorADC3 = analogRead(motorVoltagePin)
                   + analogRead(motorVoltagePin) + analogRead(motorVoltagePin);
  int VpwmADC3 = analogRead(pwmVoltagePin)
                 + analogRead(pwmVoltagePin) + analogRead(pwmVoltagePin);
  float motorSpd = 0.16667 * float(VmotorADC3 - (VpwmADC3 - VmotorADC3));

  //Update pastError
  for (int i = pastSize - 1; i > 0; i--) {
    pastError[i] = pastError[i - 1];
  }
  // Calculate the error and assign the error as the recent error
  float error = direct - motorSpd;
  pastError[0] = error;



  // Calculate the derivative for the derivative controller and calculate the sum for integral controller
  float delta = (pastError[0] - pastError[pastSize - 1]) / (pastSize * float(duration) * 1e-3);
  // sum = min(max(sum + error * float(duration) * 1e-3, -1 * maxSum), maxSum);
  //float delta = (pastError[0] - pastError[pastSize-1])/(pastSize*(float(deltaT)*1e-6));
  sum = min(max(sum + error * float(deltaT) * 1e-6, -1 * maxSum), maxSum);	//sum initialized edilmesi gerekiyo bence

  // Compute and limit the motor output command.
  int motorCmd = int(direct + Kp * error + Ki * sum + Kd * delta); //
  motorCmd = max(min(motorCmd, dacMax), 0);

  //Stops the motor.
  if (enable_pwm == 0) {
    motorCmd = 0;
  }

  analogWrite(motorOutputPin, motorCmd);
*/
  /***********************************************/
  //Do not use any other Serial.print code while using the GUI.
  //If you want to see any variable changes through serial monitor of Arduino IDE,
  //do not use the GUI.
  //Only use this(**) line and comment the
  //belows when you are tuning the angle of the arm on part 2.
  //**Serial.println(ang);
float error = 12.0 ;
float motorSpd = 45.0;
float motorCmd = Kp;
  Serial.print(t / 1000.0); // Sends the data to serial port.
  Serial.print(" , ");
  Serial.print(error); // Sends the data to serial port.
  Serial.print(" , ");
  Serial.print(motorSpd);// Sends the data to serial port.
  Serial.print(" , ");
  Serial.print(motorCmd); // Sends the data to serial port.
  Serial.print(" , ");
  Serial.print(Kp); // Sends the data to serial port.
  Serial.print(" , ");
  Serial.print(Kd);// Sends the data to serial port.
  Serial.print(" , ");
  Serial.print(Ki); // Sends the data to serial port.
  Serial.print(" , ");
  Serial.println(desired); // Sends the data to serial port.*/
  delay(50);
}
