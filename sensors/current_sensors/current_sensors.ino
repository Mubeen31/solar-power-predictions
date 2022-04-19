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
//  float current = (voltage - 2.5)/0.066;
//  Serial.print("Current : ");
//  Serial.print(current);
//  Serial.print(" ");
//  Serial.println(voltage);
//  delay(1000);
//}
/*
  ACS712 DC Current Demonstration
  acs712-dc-demo.ino
  Read current using ACS712 Hall Effect sensor
  
  DroneBot Workshop 2021
  https://dronebotworkshop.com
*/
 
// Variables for Measured Voltage and Calculated Current
double Vout = 0;
double Current = 0;
 
// Constants for Scale Factor
// Use one that matches your version of ACS712
 
//const double scale_factor = 0.185; // 5A
//const double scale_factor = 0.1; // 20A
const double scale_factor = 0.066; // 30A
 
// Constants for A/D converter resolution
// Arduino has 10-bit ADC, so 1024 possible values
// Reference voltage is 5V if not using AREF external reference
// Zero point is half of Reference Voltage
 
const double vRef = 5.00;
const double resConvert = 1024;
double resADC = vRef/resConvert;
double zeroPoint = vRef/2;
 
 
void setup(){ 
  Serial.begin(9600);
}
 
void loop(){
  
  // Vout is read 1000 Times for precision
  for(int i = 0; i < 1000; i++) {
    Vout = (Vout + (resADC * analogRead(A1)));   
    delay(1);
  }
  
  // Get Vout in mv
  Vout = Vout /1000;
  
  // Convert Vout into Current using Scale Factor
  Current = (Vout - zeroPoint)/ scale_factor + 0.12;                   
 
  // Print Vout and Current to two Current = ");                  
 
  Serial.print("Vout = ");           
  Serial.print(Vout,2); 
  Serial.print(" Volts");                            
  Serial.print("\t Current = ");                  
  Serial.print(Current,2);
  Serial.println(" Amps");                             
  delay(1000); 
}
