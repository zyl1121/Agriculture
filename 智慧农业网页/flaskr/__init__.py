from flask import Flask, request, render_template, session
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
    # hum=result.get('attr').get('hum')
    # sunlight=result.get('attr').get('sunlight')
    # soil_h=result.get('attr').get('soil_h')
    # temperature=result.get('attr').get('temprature')
    # TODO:转换时间：time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(1623663079))
    ans = result.get('attr')
    ans['update_time']=time.strftime("%m-%d %H:%M:%S", time.localtime(result.get('updated_at')))
    print(ans)
    return ans


def create_app(test_config=None):
    # create and configure the app
    # 官方文档的解释时，当你只使用单一模块时，Flask(name)会确保是正确的。
    # 如果你使用的是一个包，那么需要用到如下的两种用法之一：
    # app = Flask(‘yourapplication’)
    # app = Flask(name.split(’.’)[0])
    # https://blog.csdn.net/weixin_39165863/article/details/91492760

    app = Flask('flaskr', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='abcdefg',
        static_url_path="./static",
        static_folder='static',
    )

    @app.route('/index', methods=['GET'])
    def index():
        return render_template('index.html', data=get_data())

    return app
