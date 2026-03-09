FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    build-essential \
    libgl1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install -r requirements.txt --root-user-action=ignore

CMD ["python", "bot.py"]
