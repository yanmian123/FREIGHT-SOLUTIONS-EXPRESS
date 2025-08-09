# 使用官方 Python 3.12 slim 镜像
FROM python:3.12

# 设置环境变量：禁止写 .pyc 和启用标准输出
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 设置工作目录
WORKDIR /app

# 安装系统依赖（包括完整的 distutils）
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        python3-full &&  rm -rf /var/lib/apt/lists/*

# 先复制并安装 Python 依赖（利用 Docker 缓存）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 创建非 root 用户以提升安全性
#RUN useradd --create-home --shell /bin/bash appuser && \
#    chown -R appuser:appuser /app
#USER appuser

# 暴露端口
EXPOSE 8000

# 启动 Django 开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
