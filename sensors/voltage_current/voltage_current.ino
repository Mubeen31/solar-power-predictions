///////solar voltage//////
const int voltageSensor = A0;
float vOUT = 0.0;
float vIN = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
int value = 0;
///////solar voltage//////

///////solar current//////
// Variables for Measured Voltage and Calculated Current
double Vout = 0;
double Current = 0;
double zeroValue = 0;
 
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
///////solar current//////

///////wind current//////
// Variables for Measured Voltage and Calculated Current
double Vout1 = 0;
double Current1 = 0;
double zeroValue1 = 0;
 
// Constants for Scale Factor
// Use one that matches your version of ACS712
 
//const double scale_factor = 0.185; // 5A
//const double scale_factor = 0.1; // 20A
const double scale_factor1 = 0.066; // 30A
 
// Constants for A/D converter resolution
// Arduino has 10-bit ADC, so 1024 possible values
// Reference voltage is 5V if not using AREF external reference
// Zero point is half of Reference Voltage
 
const double vRef1 = 5.00;
const double resConvert1 = 1024;
double resADC1 = vRef1/resConvert1;
double zeroPoint1 = vRef1/2;
///////wind current//////

void setup() {
  Serial.begin(9600);
}

void loop(){
///////solar voltage//////
  value = analogRead(voltageSensor);
  vOUT = (value * 5.0) / 1024.0;
  vIN = vOUT / (R2/(R1+R2));
  Serial.print(vIN, 5);
///////solar voltage//////
  
///////solar current//////
  // Vout is read 1000 Times for precision
  for(int i = 0; i < 1000; i++) {
    Vout = (Vout + (resADC * analogRead(A1)));   
//    delay(1);
  }
  
  // Get Vout in mv
  Vout = Vout /1000;
  
  // Convert Vout into Current using Scale Factor
  Current = (Vout - zeroPoint)/ scale_factor;
  if(Current < zeroValue){
  Serial.print(" , ");                  
  Serial.print(zeroValue,5);                                   
  }
  else {
  Serial.print(" , ");                  
  Serial.print(Current,5);
  }
///////solar current//////

///////wind current//////
  // Vout is read 1000 Times for precision
  for(int i = 0; i < 1000; i++) {
    Vout1 = (Vout1 + (resADC1 * analogRead(A2)));   
//    delay(1);
  }
  
  // Get Vout in mv
  Vout1 = Vout1 /1000;
  
  // Convert Vout into Current using Scale Factor
  Current1 = (Vout1 - zeroPoint1)/ scale_factor1;
  if(Current1 < zeroValue1){
  Serial.print(" , ");                  
  Serial.println(zeroValue1,5);                                   
  }
  else {
  Serial.print(" , ");                  
  Serial.println(Current1,5);
  }
///////wind current//////
  delay(60000);
}
