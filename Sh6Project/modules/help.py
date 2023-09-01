# Credits: @cmrkuro
# Copyright (C) 2023 PyroSupra-Userbot
#
# This file is a part of < https://github.com/Sh6Kuro/PyroSupra-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Sh6Kuro/PyroSupra-Userbot/blob/main/LICENSE/>.
#
# t.me/cemarasupport & t.me/Kat4logXcode

from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from Sh6Project import CMD_HELP
from Sh6Project.helpers.basic import edit_or_reply
from Sh6Project.helpers.utility import split_list


@Client.on_message(filters.command("help", CMD_HANDLER) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        ac = PrettyTable()
        ac.header = False
        ac.title = "PyroSupra-UserBot Modules"
        ac.align = "l"
        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])
        await edit_or_reply(
            message, f"```{str(ac)}```\n• @Kat4logXcode × @Cemarasupport •"
        )
        await message.reply(
            f"**Contoh Ketik** `{CMD_HANDLER}help afk` **Untuk Melihat Informasi Module**"
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **Help For {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **Command:** `{CMD_HANDLER}{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
            this_command += "© @Kat4logXcode"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **Bukan Nama Modul yang Valid.**",
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
