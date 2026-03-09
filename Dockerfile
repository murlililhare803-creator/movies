FROM python:3.10-slim

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

RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
