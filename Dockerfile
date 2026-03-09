FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip --root-user-action=ignore \
    && pip install -r requirements.txt --root-user-action=ignore

CMD ["python", "bot.py"]
