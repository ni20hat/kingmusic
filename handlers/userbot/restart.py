# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


import os
import sys
from pyrogram.types import Message
from helpers.command import commandpro
from pyrogram import Client
from os import system, execle, environ
from helpers.decorators import errors, sudo_users_only


@Client.on_message(commandpro(["R", "!restart", ".restart", "Restart", "/restart"]))
@errors
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n✅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)
    return