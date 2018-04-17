#include <Stepper.h>
#include <Servo.h>

Servo spinWheel;
const int stepsPerRevolution = 200;
int numOfSteps;
String direction;
String value;

Stepper leftWheel(stepsPerRevolution, 8, 9, 10, 11);
Stepper rightWheel(stepsPerRevolution, 4, 5, 6, 7);

void setup() 
{
  spinWheel.attach(12);
  Serial.begin(9600);
  setStepperSpeed(170);
}

void loop()
{
 while (Serial.available()) 
 {
   split(Serial.readString());
   if(direction == "FORWARD")
   {
     forward(numOfSteps);
   }
   else if (direction == "BACK")
   {
     reverse(numOfSteps);
   }
   else if (direction == "LEFT")
   {
     left(numOfSteps);
   }
   else if (direction == "RIGHT")
   {
     right(numOfSteps);
   }
   else if(direction == "STOP")
   {
     stop();
   }
   else if(direction == "TURNFLAG")
   {
     raiseFlag(numOfSteps);
   }

  }
}

void forward(int steps)
{
  for (int i = 0; i < steps; ++i)
  {
    leftWheel.step(1);
    rightWheel.step(-1);
  }
  Serial.write("1");
//  Serial.print("Direction: Forward | Number of Steps: ");
//  Serial.print(steps);
//  Serial.println();
}

void reverse(int steps)
{
  for (int i = 0; i < steps; ++i)
  {
    leftWheel.step(-1);
    rightWheel.step(-1);
  }
  Serial.write("1");
//  Serial.println("Direction: Reverse | Number of Steps: ");
//  Serial.print(steps);
//  Serial.println();
}

void left(int steps)
{
  for (int i = 0; i < steps; ++i)
  {
    leftWheel.step(-1);
    rightWheel.step(1);
  }
  Serial.write("1");
//  Serial.println("Direction: Left | Number of Steps: ");
//  Serial.print(steps);
//  Serial.println();
}

void right(int steps)
{
  for (int i = 0; i < steps; ++i)
  {
    leftWheel.step(-1);
    rightWheel.step(1);
  }
  Serial.write("1");
//  Serial.println("Direction: Right | Number of Steps: ");
//  Serial.print(steps);
//  Serial.println();
}

void stop()
{
  leftWheel.step(0);
  rightWheel.step(0);
  Serial.write("1");
  
}

void raiseFlag(int turns) {
  
  spinWheel.write(180);
  delay(int(1170*turns));
  spinWheel.detach();
  Serial.write('1');
}

void setStepperSpeed(uint8_t speed)
{
  leftWheel.setSpeed(speed);
  rightWheel.setSpeed(speed);
}

void split(String string)
{
  for (int i = 0; i < string.length(); i++) 
  {
    if (string.substring(i, i+1) == ",") 
    {
      direction = string.substring(0, i);
      numOfSteps = string.substring(i+1).toInt();
      break;
    }
  }
}

