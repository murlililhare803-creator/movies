FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "bot.py"]
