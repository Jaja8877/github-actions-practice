from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import datetime

app = Flask(__name__)

# 定義一個計數器：紀錄訪問次數
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests to the app')

@app.route('/')
def hello_world():
    # 每次有人訪問，計數器就 +1
    REQUEST_COUNT.inc()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello, DevOps!</h1><p>訪問時間: {async_time_now(now)}</p>"

def async_time_now(t):
    return t

@app.route('/metrics')
def metrics():
    # 這是關鍵！讓 Prometheus 可以抓取數據的入口
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
