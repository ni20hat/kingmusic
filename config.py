# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 | @HYPER_AD13 | @ShiningOff
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_USERNAME = getenv("OWNER_USERNAME", "Shailendra34")
BOT_USERNAME = getenv("BOT_USERNAME", "HeroMusics_Bot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Yaaro_ki_yaarii")
BOT_NAME = getenv("BOT_NAME","𝐇𝐞𝐫𝐨 𝐌𝐮𝐬𝐢𝐜𝐬 𝐁𝐨𝐭")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
