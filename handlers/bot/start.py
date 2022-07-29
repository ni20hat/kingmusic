from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Star Müzik tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""🌟 𝖬𝖾𝗋𝗁𝖺𝖻𝖺 {message.from_user.mention} \n\n▫️ 𝖡𝖾𝗇 {bot} !\n\n▫️ 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . ! \n\n▫️ 𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 🎉", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 ", url="https://t.me/Starbotdestek"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>🇹🇷 Tüm Komutlar : \n\n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇹🇷 𝖠𝗌𝗂𝗌𝗍𝖺𝗇", url="https://t.me/StarMuzikAsistan"
                     ),
                     InlineKeyboardButton(
                         "🧑🏻‍💻 𝖮𝗐𝗇𝖾𝗋", url="https://t.me/Hayiboo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ 𝖦𝖾𝗋𝗂 ⬅️", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""🌟 𝖬𝖾𝗋𝗁𝖺𝖻𝖺 {query.from_user.mention} \n\n▫️ 𝖡𝖾𝗇 {bot} !\n\n● 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . ! \n\n▫️ 𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 🎉", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url=f"https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📝 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 ", url="https://t.me/Starbotdestek"
                    )
                ]
                
           ]
        ),
    )
