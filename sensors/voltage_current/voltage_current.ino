///////voltage//////
const int voltageSensor = A0;
float vOUT = 0.0;
float vIN = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
int value = 0;
///////voltage//////

///////current//////
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
///////current//////

void setup() {
  Serial.begin(9600);
}

void loop(){
///////voltage//////
  value = analogRead(voltageSensor);
  vOUT = (value * 5.0) / 1024.0;
  vIN = vOUT / (R2/(R1+R2));
  Serial.print(vIN, 5);
///////voltage//////
  
///////current//////
  // Vout is read 1000 Times for precision
  for(int i = 0; i < 1000; i++) {
    Vout = (Vout + (resADC * analogRead(A1)));   
//    delay(1);
  }
  
  // Get Vout in mv
  Vout = Vout /1000;
  
  // Convert Vout into Current using Scale Factor
  Current = (Vout - zeroPoint)/ scale_factor;
//  Current = (zeroPoint - Vout)/ scale_factor;                                   
  Serial.print(" , ");                  
  Serial.println(Current,5);
///////current//////
  delay(1000);
}
