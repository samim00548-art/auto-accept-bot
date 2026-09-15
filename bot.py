import os
import threading
from flask import Flask
from pyrogram import Client
from pyrogram.types import ChatJoinRequest

# UptimeRobot & Render-এর জন্য Flask Web Server
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is Alive and Running!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

# ----------------- TELEGRAM BOT CONFIG ----------------- #
# আপনার আসল API_ID, API_HASH এবং BOT_TOKEN বসান:
api_id = 32063796                     # এখানে আপনার আসল API ID (সংখ্যায়) দিন
api_hash = "4e224e4cf56b771fb2656fbbdffe1b25"       # এখানে আপনার API Hash দিন
bot_token = "8910522047:AAHZCV5GS1tiN9vQAM-DF_Mls1KiJ03-2pA"     # এখানে BotFather থেকে পাওয়া Token দিন
# -------------------------------------------------------- #

app = Client("AutoAcceptBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# যখন কেউ চ্যানেলে/গ্রুপে জয়েন রিকোয়েস্ট পাঠাবে
@app.on_chat_join_request()
async def auto_accept(client: Client, request: ChatJoinRequest):
    try:
        await client.approve_chat_join_request(
            chat_id=request.chat.id,
            user_id=request.from_user.id
        )
        print(f"অ্যাক্সেপ্ট করা হয়েছে: {request.from_user.first_name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # ব্যাকগ্রাউন্ডে ওয়েব সার্ভার চালু করা হচ্ছে
    threading.Thread(target=run_web, daemon=True).start()
    print("বট সফলভাবে চালু হয়েছে... রিকোয়েস্টের জন্য অপেক্ষা করছে!")
    app.run()