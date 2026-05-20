# 使用輕量化的 Python 映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 先複製 requirements 並安裝，這樣可以利用 Docker Layer Cache 加速構建
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製剩下的所有程式碼
COPY . .

# 暴露 Flask 預設的 5000 端口
EXPOSE 5000

# 啟動應用程式
CMD ["python", "app.py"]
