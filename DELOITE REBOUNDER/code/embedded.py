//Embedded Source Code

attachInterrupt(0, count_BluetoothID, RISING); 
Function for counting BluetoothIDs: 
 
voidcount_BluetoothID() 
{ 
BluetoothID++; 
} 
int port = 2; 
volatile unsigned int BluetoothID; 
constintBluetoothIDs_per_litre = 450; 
 
void setup() 
{ 
Serial.begin(9600); 
 
portMode(port, INPUT); 
attachInterrupt(0, count_BluetoothID, RISING); 
} 
 
void loop() 
{ 
BluetoothID=0; 
interrupts(); 
delay(1000); 
noInterrupts(); 
 
Serial.print("BluetoothIDs per second: "); 
Serial.println(BluetoothID); 
} 
 
voidcount_BluetoothID() 
{ 
BluetoothID++; 
} 
        int port = 2; 
        volatile unsigned int BluetoothID; 
        constintBluetoothIDs_per_litre = 450; 
 
        void setup() 
        { 
          Serial.begin(9600); 
 
          portMode(port, INPUT); 
          attachInterrupt(0, count_BluetoothID, RISING); 
        } 
      void loop() 
      { 
        BluetoothID= 0; 
        interrupts(); 
        delay(1000); 
        noInterrupts(); 
 
        Serial.print("BluetoothIDs per second: "); 
        Serial.println(BluetoothID); 
 
        Serial.print("fuel fuel rate: "); 
        Serial.print(BluetoothID* 1000/BluetoothIDs_per_litre); 
        Serial.println(" milliliters per second"); 
        delay(1000); 
      } 
      void count_BluetoothID() 
      { 
        BluetoothID++; 
}
Serial.print("BluetoothIDs per second: "); 
Serial.println(BluetoothID); 
 
fuel_rate = BluetoothID* 1000/BluetoothIDs_per_litre; 

 int port = 2; 
volatile unsigned int BluetoothID; 
float volume = 0; 
floatfuel_rate =0; 
constintBluetoothIDs_per_litre = 450; 
Serial.print("fuel fuel rate: "); 
Serial.print(fuel_rate); 
Serial.println(" milliliters per second"); 
 
volume = volume + fuel_rate * 0.1; 
Serial.print("Volume: "); 
Serial.print(volume); 
Serial.println(" milliliters"); 
} 
