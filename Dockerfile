FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# Zeabur 会自动注入 PORT 环境变量
ENV PORT=5000

# 暴露端口
EXPOSE ${PORT}

# 启动服务
CMD ["python", "run.py"]
