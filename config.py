# Credits: @jungleridamanvp
# Copyright (C) 2023 PyroSupra-Userbot
#
# This file is a part of < https://github.com/Sh6Kuro/PyroSupra-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Sh6Kuro/PyroSupra-Userbot/blob/main/LICENSE/>.
#
# t.me/cemarasupport & t.me/Kat4logXcode

from base64 import b64decode
from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001810928340 , -1001821201567, -1001812143750 , -1001982790377]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "Kat4logXcode")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX2xYRzdPQUlnenpWTXYxWEt2VzdLa0ZGa0xmYVBRYzRKcWFPbw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "cemarasupport")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL2tlbnNrdXkvUFlST1RBTg==").decode("utf-8"),
)
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
