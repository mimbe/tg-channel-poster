import asyncio
from telegram import Bot


BOT_TOKEN = "8230022888:AAGhP0tx3FORETo7lckbSWYay4gBb3qxNOk"

CHAT_ID = "@GulfWar3"   

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ اتصال موفق بود. کانال پابلیک است و بات می‌تواند پست کند.",
        disable_web_page_preview=True
    )

asyncio.run(main())