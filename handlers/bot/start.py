# ππππ ππππ ππππ πππππ πππππππππ @nihat_33 | 
# ππππ« πππ«π¨ π©π©π₯π¬ ππ₯π’π¬π‘ ππ¨π§'π­ π«ππ¦π¨π―π π­π‘π’π¬ π₯π’π§π ππ«π¨π¦ π‘ππ«π π


from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """**β­ Salam {}\n\nβ«οΈMΙn {} \n\nβ«οΈMΙn SadΙ Musiqi Botuyam.\n\nβ«οΈMΙni Qrupunuza ΙlavΙ edib , Admin yetkisi verΙrΙk musiqidΙn hΙzz alΔ±n !**"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="π QRUPA ΖLAVΖ ET π", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="π Sahibim ", url=f"https://t.me/nihat_33"),
                    InlineKeyboardButton(text="π¦πΏ Sohbet Qrupu ", url="https://t.me/king_sohbet_33"),
                ],                
                [                    
                    InlineKeyboardButton(text="π TΓΌm Komutlar ", url="https://t.me/gunes_isigi_33"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("hsusueue"))
def help_(bot, message):
    HELP_TXT = """Salam {}\nsorΔu yardΔ±m menyusu \nMusiqidΙn hΙzz almaΔa onu @{} qrupuna ΙlavΙ etmΙklΙ baΕlaya bilΙrsiniz probleminiz nΙdir?  π«"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="πΉοΈ Ζsas ΙmrlΙr", callback_data="basic_"),
            InlineKeyboardButton(text="πΉοΈ Admin ΙmrlΙri", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="π baΔla", callback_data="close_"),
            InlineKeyboardButton(text="β¬οΈ Geri", callback_data="HOME"),
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
    
        HELP_TXT = f"""Salam burada yardΔ±m menyusu seΓ§iminizi seΓ§in vΙ araΕdΔ±rΔ±n \nHΙr hansΔ± yardΔ±m vΙ ya problem ΓΌΓ§ΓΌn qoΕulun @{SUPPORT_GROUP} Probleminiz nΙdir π«?"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="πΉοΈ Ζsas ΙmrlΙri", callback_data="bcd"),
                InlineKeyboardButton(text="πΉοΈ Admin ΖmrlΙri", callback_data="admin"),
            ],
            [
                InlineKeyboardButton(text="π bagla", callback_data="close_"),
                InlineKeyboardButton(text="β¬οΈ Geri", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""Salam, mΙn {BOT_NAME} \nBu, sadΙ vΙ gecikmΙsiz bir botdur\nHΙr hansΔ± probleminiz varsa, qoΕulun π @{SUPPORT_GROUP}\nvΙ ya kΓΆmΙk dΓΌymΙsini basΔ±n /help """
        START_BUTTON = [
                [
                    InlineKeyboardButton(text="Sohbet π«", url=f"https://t.me/king_sohbet_33"),
                    InlineKeyboardButton(text="Qrupa ΙlavΙ et β", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="Sahibim β­", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="Sahibim β¨", url="https://t.me/nihat_33"),
                ],                
                [                    
                    InlineKeyboardButton(text="ΖmrlΙr πΉοΈ", callback_data="help_"),
                ],
                
            ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "bcd":
        B_HELP = """
`Κα΄sΙͺα΄ α΄α΄α΄α΄α΄Ι΄α΄s :- `

/play (SorΔu, YouTube linki, sΙs dosyasΔ± ) - bu ΙmrdΙn istifadΙ edib musiqidΙn hΙzz alin. 
/ytp (sorgu) - Daha ΙtraflΔ± musiqi axtarmaq ΓΌΓ§ΓΌn istifadΙ edin
/song (Sorgu) -Bu ΙmrlΙ sevimli mahnΔ±larΔ±nΔ±zΔ± yΓΌklΙyΙ bilΙrsiniz
/ara (sorgu) - YouTube dΙ axtarΔ±Ε edΙr 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="π baΔla", callback_data="close_"),
                InlineKeyboardButton(text="β¬οΈ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin":
        A_HELP = """
`Admin ΙmrlΙri :-`

/pause - Musiqinin ifasΔ±nΔ± dayandΔ±rΔ±r
/resume - DayandΔ±rΔ±lmΔ±Ε musiqini davam etdirir
/skip - nΓΆvbΙti mahnΔ±ya keΓ§id edΙr 
/end - musiqini sonlandΔ±rΔ±r
/qosul - asistanΔ± qrupa ΙlavΙ et


`Sudo ΙmrlΙri :-`

/rmf - DosyayΔ± veri tabanΔ±ndan temizler 
/rmw - Veri tabanΔ±nΔ±ndan ham dosyalarΔ± temizler
/clean - DosyalarΔ± sunucudan temizler
/gcast - kΓΌresel mesaj yayΔ±nlamak iΓ§in 
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="π bagla", callback_data="close_"),
                InlineKeyboardButton(text="β¬οΈ Geri", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
