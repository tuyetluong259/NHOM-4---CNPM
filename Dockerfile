# Sử dụng Python base image
FROM python:3.12-slim

# Đặt thư mục làm việc
WORKDIR /app

# Cài đặt các gói hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy tệp yêu cầu và cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn dự án
COPY . .

# Expose cổng 9000
EXPOSE 9000

# Chạy lệnh khởi động server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
