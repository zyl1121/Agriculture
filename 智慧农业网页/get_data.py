import requests
url = "https://api.gizwits.com/app/devdata/qUo8ZNe7YlXyIQ0rFyGpms/latest"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    "X-Gizwits-Application-Id": "e813d95a0dbc4392add7d4ff93c2e14d",
    'Connection':'keep-alive'
}
response=requests.get(url,headers=headers)
response.encoding='utf-8'
result=eval(response.text)
hum=result.get('attr').get('hum')
sunlight=result.get('attr').get('sunlight')
soil_h=result.get('attr').get('soil_h')
temperature=result.get('attr').get('temprature')
print(hum,sunlight,soil_h,temperature)