import os
from pyrogram import Client, filters
from imdb import IMDb
from motor.motor_asyncio import AsyncIOMotorClient

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

DATABASE_URI = os.environ.get("DATABASE_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

CHANNEL = int(os.environ.get("CHANNELS"))
ADMINS = [int(x) for x in os.environ.get("ADMINS").split()]

mongo = AsyncIOMotorClient(DATABASE_URI)
db = mongo[DATABASE_NAME]

imdb = IMDb()

app = Client(
    "moviebot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🎬 Welcome to Movie Bot\n\nSend me a movie name to search."
    )

@app.on_message(filters.text & ~filters.command(["start"]))
async def search_movie(client, message):

    query = message.text
    results = imdb.search_movie(query)

    if not results:
        await message.reply_text("❌ Movie not found")
        return

    movie = results[0]
    imdb_id = movie.movieID

    movie_data = imdb.get_movie(imdb_id)

    title = movie_data.get("title")
    year = movie_data.get("year")
    rating = movie_data.get("rating")
    plot = movie_data.get("plot outline")

    text = f"""
🎬 **{title} ({year})**

⭐ Rating: {rating}

📖 {plot}

🔎 Requested by: {message.from_user.mention}
"""

    await message.reply_text(text)

app.run()
