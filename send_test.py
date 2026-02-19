import asyncio
import os
from telegram import Bot

async def main():
    bot = Bot(token=os.environ["BOT_TOKEN"])
    chat_id = os.environ["CHAT_ID"]  # e.g. @YourPublicChannel
    await bot.send_message(
        chat_id=chat_id,
        text="✅ پیام تست از GitHub Actions رسید.",
        disable_web_page_preview=True,
    )

if __name__ == "__main__":
    asyncio.run(main())
