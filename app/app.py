from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 取得目前的系統時間，證明它是新的部署
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Hello, DevOps!</h1>
    <p>部署時間: {now}</p>
    <p>狀態: 運行中 ✅</p>
    <p>這是一個透過 CI/CD 自動更新的 Flask 應用程式。</p>
    """

if __name__ == '__main__':
    # 注意：必須監聽 0.0.0.0，Docker 才能連進來
    app.run(host='0.0.0.0', port=5000)
