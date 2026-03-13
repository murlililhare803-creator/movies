import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

DATABASE_URI = os.environ.get("DATABASE_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

CHANNELS = int(os.environ.get("CHANNELS"))
ADMINS = [int(x) for x in os.environ.get("ADMINS").split()]
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
