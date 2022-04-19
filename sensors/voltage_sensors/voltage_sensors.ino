const int voltageSensor = A0;

float vOUT = 0.0;
float vIN = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
int value = 0;

void setup() {
  Serial.begin(9600);
}

void loop()
{
  value = analogRead(voltageSensor);
  vOUT = (value * 5.0) / 1024.0;
  vIN = vOUT / (R2/(R1+R2)) - 0.50;
  Serial.print("Input = ");
  Serial.println(vIN);
  delay(1000);
}

//int offset = 0;// set the correction offset value
//void setup() {
//  // Robojax.com voltage sensor
//  Serial.begin(9600);
//}
//
//void loop() {
//  // Robojax.com voltage sensor
//  int volt = analogRead(A0);// read the input
//  double voltage = map(volt,0,1023, 0, 2500) + offset;// map 0-1023 to 0-2500 and add correction offset
//  
//  voltage /=100;// divide by 100 to get the decimal values
//  double voltage1 = voltage - 0.50;
//  Serial.print("Voltage: ");
//  Serial.print(voltage1);//print the voltge
//  Serial.println("V");
//  delay(1000); 
//}

//const int voltageinputPIN = A0; //select analog input pin for voltage sensor
//const int baudRate = 9600; //sets baud rate in bits per second for serial monitor
//const int sensorreadDelay = 1000; //sensor read delay in milliseconds
//const int maxanalogValue = 1010; //highest integer given at max input voltage
//const int sensormaxVoltage = 25; //highest input voltage of sensor being used
//
//float analogVoltage = 0; //to store voltage value at analog pin
//
//void setup() //setup routine runs once when reset or turned on
//{
//  Serial.begin(baudRate); //initializes serial communication
//}
//
//void loop() //loop routine runs over and over again forever
//{
//  analogVoltage = analogRead(voltageinputPIN); //reads analog voltage of incoming sensor
//  analogVoltage = (analogVoltage/maxanalogValue)*sensormaxVoltage; //conversion equation
//  Serial.print(analogVoltage); //prints value to serial monitor
//  Serial.println("V"); //prints label
//  delay(sensorreadDelay); //delay in milliseconds between read values
//}
