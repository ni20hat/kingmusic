from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["qosul"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Əvvəlcə Məni Admin etməlisən</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Kingmusic Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"•> **İstəyinizlə Gəldim** !")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistent Artıq Qrupdadır</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>{user.first_name}-ə qoşulmaq üçün çoxlu sorğulara görə Assistent qrupunuza qoşula bilmədi!  Köməkçinin qrupda qadağan edilmədiyinə əmin olun."
             "Və ya Özünüzü Qruplaşdırmaq üçün Köməkçi Hesabı əlavə edin </b>",
        )
        return
    await message.reply_text(
            "<b>Assistent Artıq Qrupdadır</b>",
        )
    
@USER.on_message(filters.group & filters.command(["cix"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>İstifadəçi qrupunuzu tərk edə bilməz!."
             "\n\nYoxsa Onu Özünüz Silə bilərsiniz</b>",
        )
        return
