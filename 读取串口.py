import time
import serial
import signal


def my_handler(signum, frame):
    global stop
    stop = True


ser = serial.Serial(
    # 端口号
    port='COM4',
    # 波特率
    baudrate=9600,
    # 校验位
    parity=serial.PARITY_ODD,
    # 停止位
    stopbits=serial.STOPBITS_TWO,
    # 数据位
    bytesize=serial.SEVENBITS)

cnt = 1
stop = False
signal.signal(signal.SIGINT, my_handler)
signal.signal(signal.SIGTERM, my_handler)
filename='test.txt'

t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print("开始时间:",t)
with open(filename, 'a') as f:
    f.write("开始时间:")
    f.write(t)
    f.write('\n')
while not stop:
    if not stop:
        received = ser.readline()
        data = received.decode('utf-8')
        data = data[data.find('{')::]
        data = eval(data)
        temp = data['T']
        hum = data['H']
        soil_h = data['Soil']
        sunlight = data['Sunlight']
        print("{}:{},{},{},{}".format(cnt, temp, hum, soil_h, sunlight))
        cnt += 1
        # t = time.time()
        # ct = time.ctime(t)
        # print(ct, ':')
        with open(filename, 'a') as f:
            f.write("{},{},{},{}".format(temp, hum, soil_h, sunlight))
            f.write('\n')
else:
    with open(filename, 'a') as f:
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print("停止时间:{}".format(t))
        print("共记录{}条数据".format(cnt-1))
        f.write("结束时间:")
        f.write(t)
        f.write('\n')
        f.write("共记录")
        f.write(str(cnt))
        f.write("条数据\n\n")