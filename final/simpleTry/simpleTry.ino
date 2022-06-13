#include <Gizwits.h>
#include <Wire.h>
#include <SoftwareSerial.h>
#include <SPI.h>
#include<OneWire.h>
#include<DallasTemperature.h>
#include <dht.h>
#include <LCD5110_Basic.h>

#define CS 8
#define BUS 4
#define DHT11_PIN 10
#define PIN_AO1 0   //土壤湿度引脚
#define PIN_AO2 1   //光照强度引脚

dht DHT;
const int button = 2;
OneWire onewire(BUS);
DallasTemperature sensors(&onewire);
Gizwits myGizwits;

int val;
String st = "";     //空气温度
String sh = "";     //空气湿度
String ssh = "";    //土壤湿度
String ssl = "";    //光照强度

//LCD5110
LCD5110 myGLCD(6, 5, 3, 9, 7);
extern uint8_t SmallFont[];
extern uint8_t MediumNumbers[];
extern uint8_t BigNumbers[];

/**
* Serial Init , Gizwits Init  
* @param none
* @return none
*/
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(button, INPUT);
  pinMode(PIN_AO1, INPUT);
  pinMode(PIN_AO2, INPUT);
  sensors.begin();
  myGLCD.InitLCD(); //Intializing LCD
  myGizwits.begin();
}

/**
* Arduino loop 
* @param none
* @return none
*/
void loop() {  
  int chk = DHT.read11(DHT11_PIN);
  sensors.requestTemperatures();
  float sensorValue=sensors.getTempCByIndex(0);
  myGLCD.setFont(SmallFont);
  unsigned long varW_hum = int(DHT.humidity);//Add Sensor Data Collection
  myGizwits.write(VALUE_hum, varW_hum);
  float varW_temprature = sensorValue;//Add Sensor Data Collection
  myGizwits.write(VALUE_temprature, varW_temprature);
  long varW_soil_h = analogRead(PIN_AO1);//Add Sensor Data Collection
  myGizwits.write(VALUE_soil_h, varW_soil_h);
  long varW_sunlight = analogRead(PIN_AO2);//Add Sensor Data Collection
  myGizwits.write(VALUE_sunlight, varW_sunlight);
  st = String(sensorValue);
  sh = String(int(DHT.humidity));
  ssh=String(analogRead(PIN_AO1));
  ssl=String(analogRead(PIN_AO2));
  String serial_out="{\"T\":"+st+",\"H\":"+sh+",\"Soil\":"+ssh+",\"Sunlight\":"+ssl+"}";
  Serial.println(serial_out);
  myGLCD.clrScr();
  myGLCD.print("Detecting", CENTER, 0);
  myGLCD.print("T:" + st+"C", CENTER, 8);
  myGLCD.print("H:" + sh+"%", CENTER, 16);
  myGLCD.print("Soil:"+ssh, CENTER, 24);
  myGLCD.print("Sunlight:"+ssl, CENTER, 32);
  myGizwits.process();
  delay(1000);
}
