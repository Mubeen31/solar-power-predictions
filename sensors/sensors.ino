//const int voltageSensor = A0;
//
//float vOUT = 0.0;
//float vIN = 0.0;
//float R1 = 30000.0;
//float R2 = 7500.0;
//int value = 0;
//
//void setup() {
//  Serial.begin(9600);
//}
//
//void loop()
//{
//  value = analogRead(voltageSensor);
//  vOUT = (value * 5.0) / 1024.0;
//  vIN = vOUT / (R2/(R1+R2));
//  Serial.print("Input = ");
//  Serial.println(vIN);
//  delay(1000);
//}
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
//  Serial.print("Voltage: ");
//  Serial.print(voltage);//print the voltge
//  Serial.println("V");
//delay(1000); 
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

//void setup() {
//  Serial.begin(9600);
//}
//
//void loop() {
// 
//  float average = 0;
//  for(int i = 0; i < 1000; i++) 
//  {
//    average = average + (.044 * analogRead(A1) -3.78) / 1000;
//  }
//  Serial.println(average);
//  delay(1000);  
//}
//void setup() {
//  // put your setup code here, to run once:
//  Serial.begin(9600);
//}
//void loop() {
//  // put your main code here, to run repeatedly:
//  int adc = analogRead(A1);
//  float voltage = adc*5/1023.0;
//  float current = (voltage-2.5)/0.066;
//  Serial.print("Current : ");
//  Serial.println(current);
//  delay(1000);
//}

#define VIN A1 // define the Arduino pin A0 as voltage input (V in)
const float VCC   = 5.0;// supply voltage is from 4.5 to 5.5V. Normally 5V.
const int model = 2;   // enter the model number (see below)

float cutOffLimit = 1.01;// set the current which below that value, doesn't matter. Or set 0.5

/*
          "ACS712ELCTR-05B-T",// for model use 0
          "ACS712ELCTR-20A-T",// for model use 1
          "ACS712ELCTR-30A-T"// for model use 2  
sensitivity array is holding the sensitivy of the  ACS712
current sensors. Do not change. All values are from page 5  of data sheet          
*/
float sensitivity[] ={
          0.185,// for ACS712ELCTR-05B-T
          0.100,// for ACS712ELCTR-20A-T
          0.066// for ACS712ELCTR-30A-T
     
         }; 


const float QOV =   0.5 * VCC;// set quiescent Output voltage of 0.5V
float voltage;// internal variable for voltage

void setup() {
    //Robojax.com ACS712 Current Sensor 
    Serial.begin(9600);// initialize serial monitor
    Serial.println("Robojax Tutorial");
    Serial.println("ACS712 Current Sensor");
}

void loop() {
  

  //Robojax.com ACS712 Current Sensor 
  float voltage_raw =   (5.0 / 1023.0)* analogRead(VIN);// Read the voltage from sensor
  voltage =  voltage_raw - QOV + 0.012 ;// 0.000 is a value to make voltage zero when there is no current
  float current = voltage / sensitivity[model];
 
  if(abs(current) > cutOffLimit ){
    Serial.print("V: ");
    Serial.print(voltage,3);// print voltage with 3 decimal places
    Serial.print("V, I: ");
    Serial.print(current,2); // print the current with 2 decimal places
    Serial.println("A");
  }else{
    Serial.println("No Current");
  }
  delay(1000);
}
