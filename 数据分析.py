import re
from matplotlib import pyplot as plt
import numpy as np
from time import *

humidity = []
soil_humidity=[]
temp1 = []
sunlight=[]
t = []
h = []
ocolor = 'b'
polycolor = 'r'
avgcolor = 'g'
file_name='test.txt'
font_size=14

# 提取温湿度数据
with open(file_name, 'r') as f:
    for line in f.readlines():
        if len(line.split(','))==4:
                line=line.replace('\n','')
                data=line.split(',')
                temp1.append(float(data[0]))
                humidity.append(float(data[1]))
                soil_humidity.append(int(data[2]))
                sunlight.append(int(data[3]))
                    
print(sunlight)
# 求出平均值
tavg = round(sum(temp1) / len(temp1), 1)
havg = round(sum(humidity) / len(humidity), 1)
shavg = round(sum(soil_humidity) / len(soil_humidity), 1)
savg = round(sum(sunlight) / len(sunlight), 1)
print("数据个数：{}".format(len(temp1)))

# 画曲线图
fig=plt.figure('温湿度统计',figsize=(13,9))
font = {'family': 'MicroSoft YaHei', 'size': 10}
plt.rc("font", **font)


# 1.温度曲线图
ax1=fig.add_subplot(311)
plt.suptitle('{}'.format(strftime("%Y年%m月%d日温湿度曲线图")))
plt.title("温度曲线")
plt.ylabel("摄氏度(℃)")
plt.xticks([])
x = np.array(range(len(temp1)))
y1 = np.array(temp1)
z1 = np.polyfit(x, y1, 20)
p1 = np.poly1d(z1)
poly1 = p1(x)
plot1 = ax1.plot(x, temp1, color=ocolor, label='温度',ls='dashed')
plot2 = ax1.plot(x, poly1, ls='-', color=polycolor, label='温度拟合曲线')
t1_avgline = ax1.axhline(y=tavg, ls='--', c=avgcolor, label='温度平均值:{}℃'.format(tavg))
ax1.axis([1, len(temp1), min(temp1) - 2, max(temp1) + 2])
plt.legend(fontsize=font_size-1,loc='best')

# 2.湿度曲线图
ax2=fig.add_subplot(312)
plt.title("湿度曲线")
plt.ylabel("湿度(%)")
plt.xticks([])
plt.axis([1, len(humidity), min(humidity) - 2, max(humidity) + 2])
y2 = np.array(humidity)
z2 = np.polyfit(x, y2, 20)
p2 = np.poly1d(z2)
poly2 = p2(x)
plot3 = ax2.plot(x, humidity, color=ocolor, label='湿度',ls='dashed')
plot4 = ax2.plot(x, poly2, ls='-', color=polycolor, label='湿度拟合曲线')
h_avgline = plt.axhline(y=havg, ls='--', c=avgcolor, label='湿度平均值:{}%'.format(havg))
plt.legend(fontsize=font_size-1,loc='best')


# 3.温湿度拟合图
ax3=fig.add_subplot(313)
plt.title('温湿度拟合图')
plt.xticks([])
plot5=ax3.plot(x, poly1, color="red", label="温度曲线图")
ax3.set_ylabel("温度")
ax4 = ax3.twinx()
plot6=ax4.plot(x, poly2, color="b", label="湿度曲线图")
ax4.set_ylabel("湿度")
# 合并图例
plots=plot5+plot6
plabels=[l.get_label() for l in plots]
ax3.legend(plots,plabels,loc='best',fontsize=font_size-1)

# 4.光照曲线图
fig1=plt.figure("光照强度统计",figsize=(12,8))
fig1.suptitle('{}'.format(strftime("%Y年%m月%d日光照曲线图")))
sun_gragh=fig1.add_subplot(111)
plt.ylabel("光照")
plt.xticks([])
plt.axis([1, len(sunlight), min(sunlight) - 10, max(sunlight) + 10])
y3 = np.array(sunlight)
z3 = np.polyfit(x, y3, 20)
p3 = np.poly1d(z3)
poly3 = p3(x)
sun_gragh.plot(x, y3, color=ocolor, label='光照',ls='dashed')
sun_gragh.plot(x, poly3, ls='-', color=polycolor, label='光照拟合曲线')
sl_avgline = sun_gragh.axhline(y=savg, ls='--', c=avgcolor, label='光照平均值:{}'.format(savg))
plt.legend(fontsize=font_size,loc='best')

# 5.土壤湿度曲线图
fig2=plt.figure("土壤湿度统计",figsize=(12,8))
fig2.suptitle('{}'.format(strftime("%Y年%m月%d日土壤湿度曲线图")))
plt.ylabel("土壤湿度")
plt.xticks([])
plt.axis([1, len(soil_humidity), min(soil_humidity) - 10, max(soil_humidity) + 50])
y4 = np.array(soil_humidity)
z4 = np.polyfit(x, y4, 20)
p4 = np.poly1d(z4)
poly4 = p4(x)
plt.plot(x, y4, color=ocolor, label='土壤湿度',ls='dashed')
plt.plot(x, poly4, ls='-', color=polycolor, label='土壤湿度拟合曲线',)
sh_avgline = plt.axhline(y=shavg, ls='--', c=avgcolor, label='土壤湿度平均值:{}'.format(shavg))
plt.legend(fontsize=font_size,loc='best')

fig.savefig('{}'.format(strftime("%Y年%m月%d日温湿度曲线图")))   #保存图片
fig1.savefig('{}'.format(strftime("%Y年%m月%d日光照强度统计")))   #保存图片
fig2.savefig('{}'.format(strftime("%Y年%m月%d日土壤统计")))   #保存图片
plt.show()