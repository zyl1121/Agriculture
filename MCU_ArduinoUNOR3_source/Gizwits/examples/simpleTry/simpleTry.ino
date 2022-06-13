#include <Gizwits.h>
#include <Wire.h>
#include <SoftwareSerial.h>
#include <SPI.h>
#include <SD.h>
#include<OneWire.h>
#include<DallasTemperature.h>
#include <dht.h>
#include <LCD5110_Basic.h>

#define CS 8
#define BUS 4
#define DHT11_PIN 10
#define PIN_AO1 0   //土壤湿度引脚
#define PIN_AO2 1   //光照强度引脚

SoftwareSerial mySerial(0, 1); // A2 -> RX, A3 -> TX
dht DHT;
const int button = 2;
OneWire onewire(BUS);
DallasTemperature sensors(&onewire);
File logFile;
Gizwits myGizwits;

//LCD5110
LCD5110 myGLCD(6, 5, 3, 9, 7);
extern uint8_t SmallFont[];
extern uint8_t MediumNumbers[];
extern uint8_t BigNumbers[];

boolean initCard()
{
  Serial.print("Connecting to SD card... ");
  // 初始化SD卡
  if (!SD.begin(CS))
  {
    // An error occurred
    Serial.println("\tError: Could not connect to SD card!");
    myGLCD.print("SDcard Error!", CENTER, 40);
    return false;
  }
  else
    Serial.println("Done!");
    myGLCD.clrScr();
  return true;
}


/**
* Serial Init , Gizwits Init  
* @param none
* @return none
*/
void setup() {
  // put your setup code here, to run once:

  mySerial.begin(115200);

  myGizwits.begin();

  mySerial.println("GoKit init  OK \n");
  Serial.begin(9600);
  pinMode(button, INPUT);
  pinMode(PIN_AO1, INPUT);
  pinMode(PIN_AO2, INPUT);
  sensors.begin();
  myGLCD.InitLCD(); //Intializing LCD
  initCard();
}

/**
* Arduino loop 
* @param none
* @return none
*/
void loop() {  
  
  //Configure network
  //if(XXX) //Trigger Condition
  //myGizwits.setBindMode(0x02);  //0x01:Enter AP Mode;0x02:Enter Airlink Mode
    /*
  unsigned long varW_hum = 0;//Add Sensor Data Collection
  myGizwits.write(VALUE_hum, varW_hum);
  float varW_temprature = 0;//Add Sensor Data Collection
  myGizwits.write(VALUE_temprature, varW_temprature);
  long varW_soil_h = 0;//Add Sensor Data Collection
  myGizwits.write(VALUE_soil_h, varW_soil_h);
  long varW_sunlight = 0;//Add Sensor Data Collection
  myGizwits.write(VALUE_sunlight, varW_sunlight);
  



  //binary datapoint handle
  */
 int chk = DHT.read11(DHT11_PIN);
  sensors.requestTemperatures();
  float sensorValue=sensors.getTempCByIndex(0);
  val = digitalRead(button);
  myGLCD.setFont(SmallFont);
  if (val == HIGH){
     initCard();
  }
  temprature=sensorValue;
  hum=int(DHT.humidity);
  soil_h=analogRead(PIN_AO1);
  sunlight=analogRead(PIN_AO2);
  myGizwits.write(temprature, hum, soil_h, sunlight);
    String data="";
    st = String("T:" + String(sensorValue)+"C");
    sh = String("H:" + String(int(DHT.humidity))+"%");
    ssh=String("Soil:"+String(analogRead(PIN_AO1)));
    ssl=String("Sunlight: "+String(analogRead(PIN_AO2)));
    Serial.print(st);
    Serial.print("\t");
    Serial.print(sh);
    Serial.print("\t");
    Serial.print(ssh);
    Serial.print("\t");
    Serial.println(ssl);
    logFile = SD.open("test.txt", FILE_WRITE);
    if (!logFile){
      myGLCD.print("Logging Error!", CENTER, 40);
    }
    else{
      
      data+=String(sensorValue);  //空气温度
      data+=",";
      data+=String(DHT.humidity); //空气湿度
      data+=",";
      data+=String(analogRead(PIN_AO1));  //土壤湿度 
      data+=",";
      data+=String(analogRead(PIN_AO2));  //光照强度
      logFile.println();  
      logFile.println(data);
      logFile.close();
    }
    myGLCD.clrScr();
    myGLCD.print("Detecting", CENTER, 0);
    myGLCD.print(st, CENTER, 8);
    myGLCD.print(sh, CENTER, 16);
    myGLCD.print(ssh, CENTER, 24);
    myGLCD.print(ssl, CENTER, 32);
    delay(1000);
  myGizwits.process();
}
