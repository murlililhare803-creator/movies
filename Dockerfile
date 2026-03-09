FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libffi-dev \
    build-essential
COPY . /app/
RUN pip install --upgrade pip --root-user-action=ignore \
    && pip install -r requirements.txt --root-user-action=ignore
EXPOSE 8080
CMD ["python", "bot.py"]
