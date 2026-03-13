from pyrogram import Client, filters
from imdb import IMDb
from config import *

app = Client(
    "moviebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

imdb = IMDb()

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🎬 Welcome to Movie Auto Filter Bot\n\nSend movie name to search."
    )

@app.on_message(filters.text)
async def search_movie(client, message):

    movie_name = message.text
    movies = imdb.search_movie(movie_name)

    if not movies:
        await message.reply_text("❌ Movie not found")
        return

    movie = movies[0]
    movie_id = movie.movieID
    data = imdb.get_movie(movie_id)

    title = data.get("title")
    year = data.get("year")
    rating = data.get("rating")

    text = f"""
🎬 {title} ({year})

⭐ Rating: {rating}

🔎 Requested by {message.from_user.mention}
"""

    await message.reply_text(text)

app.run()
