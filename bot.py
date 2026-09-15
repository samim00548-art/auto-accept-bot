from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

# আপনার Telegram API ID, API Hash এবং Bot Token এখানে দিন
api_id = 32063796  # আপনার API ID (integer, তাই কোটেশন ছাড়া দিন)
api_hash = "4e224e4cf56b771fb2656fbbdffe1b25"
bot_token = "8910522047:AAHZCV5GS1tiN9vQAM-DF_Mls1KiJ03-2pA"

app = Client("AutoAcceptBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# যখন কেউ চ্যানেলে জয়েন রিকোয়েস্ট পাঠাবে, তখন এই ফাংশনটি কাজ করবে
@app.on_chat_join_request()
async def auto_accept(client: Client, request: ChatJoinRequest):
    try:
        # জয়েন রিকোয়েস্ট অটো-অ্যাক্সেপ্ট করা হচ্ছে
        await client.approve_chat_join_request(
            chat_id=request.chat.id,
            user_id=request.from_user.id
        )
        print(f"{request.from_user.first_name} এর রিকোয়েস্ট অ্যাক্সেপ্ট করা হয়েছে!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("বট চালু হয়েছে... রিকোয়েস্টের জন্য অপেক্ষা করছে!")
    app.run()