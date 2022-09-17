# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @nihat_33 | 
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**⭐ Salam {}\n\n▫️Mən {} \n\n▫️Mən Sadə Musiqi Botuyam.\n\n▫️Məni Qrupunuza əlavə edib , Admin yetkisi verərək musiqidən həzz alın !**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="🎉 QRUPA ƏLAVƏ ET 🎉", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="📝 Sahibim ", url=f"https://t.me/nihat_33"),
                    InlineKeyboardButton(text="🇦🇿 Sohbet Qrupu ", url="https://t.me/king_sohbet_33"),
                ],                
                [                    
                    InlineKeyboardButton(text="📚 Tüm Komutlar ", url="https://t.me/gunes_isigi_33"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("hsusueue"))
def help_(bot, message):
    HELP_TXT = """Salam {}\nsorğu yardım menyusu \nMusiqidən həzz almağa onu @{} qrupuna əlavə etməklə başlaya bilərsiniz probleminiz nədir?  💫"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="🕹️ Əsas əmrlər", callback_data="basic_"),
            InlineKeyboardButton(text="🕹️ Admin əmrləri", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="🗑 bağla", callback_data="close_"),
            InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Salam burada yardım menyusu seçiminizi seçin və araşdırın \nHər hansı yardım və ya problem üçün qoşulun @{SUPPORT_GROUP} Probleminiz nədir 💫?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="🕹️ Əsas əmrləri", callback_data="bcd"),
                InlineKeyboardButton(text="🕹️ Admin Əmrləri", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="🗑 bagla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Salam, mən {BOT_NAME} \nBu, sadə və gecikməsiz bir botdur\nHər hansı probleminiz varsa, qoşulun 👉 @{SUPPORT_GROUP}\nvə ya kömək düyməsini basın /help """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="Sohbet 💫", url=f"https://t.me/king_sohbet_33"),
                    InlineKeyboardButton(text="Qrupa əlavə et ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim ⭐", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sahibim ✨", url="https://t.me/nihat_33"),
                ],                
                [                    
                    InlineKeyboardButton(text="Əmrlər 🕹️", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs :- `

/play (Sorğu, YouTube linki, səs dosyası ) - bu əmrdən istifadə edib musiqidən həzz alin. 
/ytp (sorgu) - Daha ətraflı musiqi axtarmaq üçün istifadə edin
/song (Sorgu) -Bu əmrlə sevimli mahnılarınızı yükləyə bilərsiniz
/ara (sorgu) - YouTube də axtarış edər 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 bağla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin əmrləri :-`

/pause - Musiqinin ifasını dayandırır
/resume - Dayandırılmış musiqini davam etdirir
/skip - növbəti mahnıya keçid edər 
/end - musiqini sonlandırır
/qosul - asistanı qrupa əlavə et


`Sudo əmrləri :-`

/rmf - Dosyayı veri tabanından temizler 
/rmw - Veri tabanınından ham dosyaları temizler
/clean - Dosyaları sunucudan temizler
/gcast - küresel mesaj yayınlamak için 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="🗑 bagla", callback_data="close_"),
                InlineKeyboardButton(text="⬅️ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
