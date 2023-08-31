# Credits: @cmrkuro
# Copyright (C) 2023 PyroSupra-Userbot
#
# This file is a part of < https://github.com/Sh6Kuro/PyroSupra-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Sh6Kuro/PyroSupra-Userbot/blob/main/LICENSE/>.
#
# t.me/cemarasupport & t.me/Kat4logXcode

import aiohttp


async def expand_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://expandurl.com/api/v1/?url={url}") as resp:
            expanded = await resp.text()

        return expanded if expanded != "false" and expanded[:-1] != url else None
