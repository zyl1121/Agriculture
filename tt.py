import time
import serial
import signal


def my_handler(signum, frame):
    global stop
    stop = True


ser = serial.Serial(
    # 端口号
    port='COM3',
    # 波特率
    baudrate=9600,
    # 校验位
    parity=serial.PARITY_ODD,
    # 停止位
    stopbits=serial.STOPBITS_TWO,
    # 数据位
    bytesize=serial.SEVENBITS)

cnt = 0
stop = False
signal.signal(signal.SIGINT, my_handler)
signal.signal(signal.SIGTERM, my_handler)


while not stop:
    received = ser.readline()
    data = received.decode('utf-8')
    data = data[data.find('{')::]
    data = eval(data)
    temp = data['T']
    hum = data['H']
    soil_h = data['Soil']
    sunlight = data['Sunlight']
    print(temp,hum,soil_h,sunlight)