import importlib
from pyrogram import idle
from uvloop import install
from aiohttp import ClientSession

from Sh6Project import LOGGER, LOOP, bots
from Sh6Project.modules import ALL_MODULES


async def main():
    # Mengimpor semua modul
    for all_module in ALL_MODULES:
        importlib.import_module(f"Sh6Project.modules.{all_module}")

    # Inisialisasi session dan mulai semua bot
    async with ClientSession() as aiosession:
        for bot in bots:
            try:
                await bot.start()
                bot.me = await bot.get_me()
                await bot.join_chat("plerkuda69")
                await bot.join_chat("pleerkuda69")
            except Exception as e:
                LOGGER("main").warning(f"Failed to start bot: {e}")

        LOGGER("Sh6Project").info(f"Pyro-UserBot v69 [🔥 BERHASIL DIAKTIFKAN! 🔥]")
        await idle()  # Menunggu sampai bot dihentikan secara manual


if __name__ == "__main__":
    LOGGER("Sh6Project").info("Starting Pyro-UserBot")
    install()  # Menginstal uvloop
    LOOP.run_until_complete(main())  # Menjalankan event loop
