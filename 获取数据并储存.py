import requests
import time


def get_data():
    url = "https://api.gizwits.com/app/devdata/qUo8ZNe7YlXyIQ0rFyGpms/latest"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        "X-Gizwits-Application-Id": "e813d95a0dbc4392add7d4ff93c2e14d",
        'Connection': 'keep-alive'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    result = eval(response.text)
    return result


last_update_time = ''
while 1:
    result = get_data()
    update_time = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(get_data().get('updated_at')))
    hum = result.get('attr').get('hum')
    sunlight = result.get('attr').get('sunlight')
    soil_h = result.get('attr').get('soil_h')
    temperature = result.get('attr').get('temprature')
    data="{},空气温度:{},空气湿度:{},土壤湿度:{},光照强度:{}".format(update_time, temperature, hum, soil_h, sunlight)
    if last_update_time != update_time:
        print(data)
        with open('log.txt', 'a') as f:
            # 以上传时间，空气温度，空气湿度，土壤湿度，光照强度顺序储存到log.txt中
            f.write(data)
            f.write('\n')
    time.sleep(5)
