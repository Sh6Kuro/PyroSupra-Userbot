# Credits: @jungleridamanvp
# Copyright (C) 2023 PyroSupra-Userbot
#
# This file is a part of < https://github.com/Sh6Kuro/PyroSupra-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Sh6Kuro/PyroSupra-Userbot/blob/main/LICENSE/>.
#
# t.me/cemarasupport & t.me/Kat4logXcode

n = "\n"
w = " "

bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "

mono = lambda x: f"`{x}`{n}"


def section(
    title: str,
    body: dict,
    indent: int = 2,
    underline: bool = False,
) -> str:
    text = (bold_ul(title) + n) if underline else bold(title) + n

    for key, value in body.items():
        text += (
            indent * w
            + bold(key)
            + ((value[0] + n) if isinstance(value, list) else mono(value))
        )
    return text
