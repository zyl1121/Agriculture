#include <dht.h>
dht DHT;
#define DHT11_PIN 5
void setup(){
  Serial.begin(9600); 
//  Serial.println("DHT TEST PROGRAM "); 
//  Serial.print("LIBRARY VERSION: ");     
//  Serial.println(DHT_LIB_VERSION); 
//  Serial.println(); 
  Serial.println("Humidity (%),\tTemperature (C)");
}

void loop(){ 
  int chk = DHT.read11(DHT11_PIN); 
  switch (chk)
  {
    case DHTLIB_OK:  
                Serial.print("OK,"); 
                break;
    case DHTLIB_ERROR_CHECKSUM: 
                Serial.print("Checksum error,"); 
                break;
    case DHTLIB_ERROR_TIMEOUT: 
                Serial.print("Time out error,"); 
                break;
    case DHTLIB_ERROR_CONNECT:
        Serial.print("Connect error,");
        break;
    case DHTLIB_ERROR_ACK_L:
        Serial.print("Ack Low error,");
        break;
    case DHTLIB_ERROR_ACK_H:
        Serial.print("Ack High error,");
        break;
    default: 
                Serial.print("Unknown error,\t"); 
                break;
  }
// DISPLAY DATA 
  Serial.print(DHT.humidity, 0); 
  Serial.print(",");
  Serial.println(DHT.temperature,0); 
  delay(2000);
}
