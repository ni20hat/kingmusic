# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 |
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.command import commandpro
from helpers.filters import other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton,
                            ReplyKeyboardMarkup, ReplyKeyboardRemove)


PAUSED = "https://telegra.ph/file/94ee2bdfc7e81d371aae3.jpg"
RESUMED = "https://telegra.ph/file/50cf13056d78898e13ae0.jpg"
SKIPPED = "https://telegra.ph/file/116d7d9b9100c44249333.jpg"
END = "https://telegra.ph/file/6d1902d08c88f318d53c7.jpg"

BUTTON = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/HeroOfficialBots"),
        InlineKeyboardButton(text="🗑️Close", callback_data="close_"),
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Yaaro_ki_yaarii"), 
    ],
]

ACTV_CALLS = []

@Client.on_message(commandpro(["/pause", "!pause", "pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    
    await message.reply_photo(
        photo=PAUSED,
        caption=f"sᴛʀᴇᴀᴍ ᴘᴀᴜsᴇᴅ ʙʏ {message.from_user.mention} 🥀\n\n✦ /resume :- ʀᴇsᴜᴍᴇ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/resume", "!resume", "resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    
    await message.reply_photo(
        photo=RESUMED,
        caption=f"ʀᴇsᴜᴍᴇᴅ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ʙʏ {message.from_user.mention} 💫.\n\n✦ /pause :- ᴘᴀᴜsᴇ ᴘʟᴀʏʙᴀᴄᴋ!!",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()


@Client.on_message(commandpro(["/end", "!end", "/stop", "!stop", "stop", "end"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chut_id = message.chat.id
    if int(chut_id) not in ACTV_CALLS:
        await message.reply_text(
            "ᴡᴛғ, ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ ғɪʀsᴛ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ sᴋɪᴘ ᴛʜᴀᴛ 💫",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    
        await message.reply_photo(
            photo=END,
            caption=f"sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ ʙʏ {message.from_user.mention} \n ɴᴏᴡ ʟᴇᴀᴠɪɴɢ ᴠᴄ ʙʏᴇ ʙʏᴇ 👋🏻",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    

@Client.on_message(commandpro(["/skip", "!skip", "skip"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        
        await message.reply_text(
            "ᴡᴛғ, ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ ғɪʀsᴛ ɪɴ ᴏʀᴅᴇʀ ᴛᴏ sᴋɪᴘ ᴛʜᴀᴛ 🙄",
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
        await message.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
    
    await message.reply_photo(
        photo=SKIPPED,
        caption=f"ᴍᴏᴠᴇᴅ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴏɴɢ\nsᴛʀᴇᴀᴍ sᴋɪᴘᴘᴇᴅ ʙʏ {message.from_user.mention}🥀",
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
    await message.delete()
