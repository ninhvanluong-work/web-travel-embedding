# --- Stage 1: Builder ---
FROM python:3.12.12-slim AS builder

# Thiết lập môi trường để tối ưu hóa Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Cài đặt các dependencies cần thiết để build (nếu có các lib cần trình biên dịch)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Tạo và cài đặt venv
RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

# --- Stage 2: Production ---
FROM python:3.12.12-slim

WORKDIR /app

# Chỉ copy venv từ stage builder sang, giúp image cực nhẹ
COPY --from=builder /app/.venv /app/.venv

# Copy source code (Lưu ý: bỏ dấu / trước app nếu file nằm cùng cấp với Dockerfile)
COPY . .

# Đảm bảo môi trường sử dụng venv
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# Chạy bằng uvicorn trực tiếp vì PATH đã được trỏ tới venv
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]