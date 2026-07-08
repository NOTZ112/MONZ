from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from database.join_reqs import JoinReqs
from config import ADMINS, FORCE_SUB_CHANNELS


@Client.on_chat_join_request(filters.chat(FORCE_SUB_CHANNELS if FORCE_SUB_CHANNELS else "self"))
async def join_reqs(client, join_req: ChatJoinRequest):

    jishubotz = JoinReqs(join_req.chat.id)

    if jishubotz.isActive():
        user_id = join_req.from_user.id
        first_name = join_req.from_user.first_name
        username = join_req.from_user.username
        date = join_req.date

        await jishubotz.add_user(
            user_id=user_id,
            first_name=first_name,
            username=username,
            date=date
        )

@Client.on_message(filters.command("total") & filters.private & filters.user(ADMINS))
async def total_requests(client, message):
    total = 0
    for channel_id in FORCE_SUB_CHANNELS:
        jishubotz = JoinReqs(channel_id)
        if jishubotz.isActive():
            total += await jishubotz.get_all_users_count()

    await message.reply_text(
        text=f"**🗿 Total Requests :** `{total}`",
        parse_mode=enums.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        quote=True)


@Client.on_message(filters.command("clear") & filters.private & filters.user(ADMINS))
async def purge_requests(client, message):
    for channel_id in FORCE_SUB_CHANNELS:
        jishubotz = JoinReqs(channel_id)
        if jishubotz.isActive():
            await jishubotz.delete_all_users()

    await message.reply_text(
        text="Cleared All Requests 🧹",
        parse_mode=enums.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        quote=True)




        
# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
