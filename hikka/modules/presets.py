# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

import asyncio
import logging

from .. import loader, utils
from ..inline.types import BotInlineMessage, InlineCall
from ..types import Message

logger = logging.getLogger(__name__)


PRESETS = {
    "fun": [
        "https://heta.dan.tatar/aniquotes.py",
        "https://heta.dan.tatar/artai.py",
        "https://heta.dan.tatar/inline_ghoul.py",
        "https://heta.dan.tatar/lovemagic.py",
        "https://heta.dan.tatar/mindgame.py",
        "https://heta.dan.tatar/moonlove.py",
        "https://heta.dan.tatar/neko.py",
        "https://heta.dan.tatar/purr.py",
        "https://heta.dan.tatar/rpmod.py",
        "https://heta.dan.tatar/scrolller.py",
        "https://heta.dan.tatar/tictactoe.py",
        "https://heta.dan.tatar/trashguy.py",
        "https://heta.dan.tatar/truth_or_dare.py",
        "https://heta.dan.tatar/sticks.py",
        "https://heta.dan.tatar/premium_sticks.py",
        "https://heta.dan.tatar/MoriSummerz/ftg-mods/magictext.py",
        "https://heta.dan.tatar/HitaloSama/FTG-modules-repo/quotes.py",
        "https://heta.dan.tatar/HitaloSama/FTG-modules-repo/spam.py",
        "https://heta.dan.tatar/SkillsAngels/Modules/IrisLab.py",
        "https://heta.dan.tatar/Fl1yd/FTG-Modules/arts.py",
        "https://heta.dan.tatar/SkillsAngels/Modules/Complements.py",
        "https://heta.dan.tatar/Den4ikSuperOstryyPer4ik/Astro-modules/Compliments.py",
        "https://heta.dan.tatar/vsecoder/hikka_modules/mazemod.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/dice.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/loli.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/DoxTool.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/randomizer.py",
    ],
    "chat": [
        "https://heta.dan.tatar/activists.py",
        "https://heta.dan.tatar/banstickers.py",
        "https://heta.dan.tatar/hikarichat.py",
        "https://heta.dan.tatar/inactive.py",
        "https://heta.dan.tatar/keyword.py",
        "https://heta.dan.tatar/tagall.py",
        "https://heta.dan.tatar/voicechat.py",
        "https://heta.dan.tatar/vtt.py",
        "https://heta.dan.tatar/SekaiYoneya/Friendly-telegram/BanMedia.py",
        "https://heta.dan.tatar/iamnalinor/FTG-modules/swmute.py",
        "https://heta.dan.tatar/GeekTG/FTG-Modules/filter.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/id.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/clickon.py",
    ],
    "service": [
        "https://heta.dan.tatar/account_switcher.py",
        "https://heta.dan.tatar/surl.py",
        "https://heta.dan.tatar/httpsc.py",
        "https://heta.dan.tatar/img2pdf.py",
        "https://heta.dan.tatar/latex.py",
        "https://heta.dan.tatar/pollplot.py",
        "https://heta.dan.tatar/sticks.py",
        "https://heta.dan.tatar/temp_chat.py",
        "https://heta.dan.tatar/vtt.py",
        "https://heta.dan.tatar/vsecoder/hikka_modules/accounttime.py",
        "https://heta.dan.tatar/vsecoder/hikka_modules/searx.py",
        "https://heta.dan.tatar/iamnalinor/FTG-modules/swmute.py",
        "https://raw.githubusercontent.com/coddrago/modules/main/modlist.py",
    ],
    "downloaders": [
        "https://heta.dan.tatar/musicdl.py",
        "https://heta.dan.tatar/uploader.py",
        "https://heta.dan.tatar/porn.py",
        "https://heta.dan.tatar/web2file.py",
        "https://heta.dan.tatar/AmoreForever/amoremods/instsave.py",
        "https://heta.dan.tatar/CakesTwix/Hikka-Modules/tikcock.py",
        "https://heta.dan.tatar/CakesTwix/Hikka-Modules/InlineYouTube.py",
        "https://heta.dan.tatar/CakesTwix/Hikka-Modules/InlineSpotifyDownloader.py",
        "https://heta.dan.tatar/GeekTG/FTG-Modules/downloader.py",
        "https://heta.dan.tatar/Den4ikSuperOstryyPer4ik/Astro-modules/dl_yt_previews.py",
    ],
}


@loader.tds
class Presets(loader.Module):
    """Suggests new Hikka users a packs of modules to load"""

    strings = {"name": "Presets"}

    async def client_ready(self):
        self._markup = utils.chunks(
            [
                {
                    "text": self.strings(f"_{preset}_title"),
                    "callback": self._preset,
                    "args": (preset,),
                }
                for preset in PRESETS
            ],
            1,
        )

        if self.get("sent"):
            return

        self.set("sent", True)
        await self._menu()

    async def _menu(self):
        await self.inline.bot.send_photo(
            self._client.tg_id,
            'https://imgur.com/a/Z6PP9as.png',
            caption=self.strings('welcome'),
            reply_markup=self.inline.generate_markup(self._markup),
        )

    async def _back(self, call: InlineCall):
        await call.edit(self.strings("welcome"), reply_markup=self._markup)

    async def _install(self, call: InlineCall, preset: str):
        await call.delete()
        m = await self._client.send_message(
            self.inline.bot_id,
            self.strings("installing").format(preset),
        )
        for i, module in enumerate(PRESETS[preset]):
            await m.edit(
                self.strings("installing_module").format(
                    preset,
                    i,
                    len(PRESETS[preset]),
                    module,
                )
            )
            try:
                await self.lookup("loader").download_and_install(module, None)
            except Exception:
                logger.exception("Failed to install module %s", module)

            await asyncio.sleep(1)

        if self.lookup("loader").fully_loaded:
            self.lookup("loader").update_modules_in_db()

        await m.edit(self.strings("installed").format(preset))
        await self._menu()

    def _is_installed(self, link: str) -> bool:
        return any(
            link.strip().lower() == installed.strip().lower()
            for installed in self.lookup("loader").get("loaded_modules", {}).values()
        )

    async def _preset(self, call: InlineCall, preset: str):
        await call.message.edit(
            self.strings("preset").format(
                self.strings(f"_{preset}_title"),
                self.strings(f"_{preset}_desc"),
                "\n".join(
                    map(
                        lambda x: x[0],
                        sorted(
                            [
                                (
                                    "{} <b>{}</b>".format(
                                        (
                                            self.strings("already_installed")
                                            if self._is_installed(link)
                                            else "▫️"
                                        ),
                                        link.rsplit("/", maxsplit=1)[1].split(".")[0],
                                    ),
                                    int(self._is_installed(link)),
                                )
                                for link in PRESETS[preset]
                            ],
                            key=lambda x: x[1],
                            reverse=True,
                        ),
                    )
                ),
            ),
            reply_markup=[
                {"text": self.strings("back"), "callback": self._back},
                {
                    "text": self.strings("install"),
                    "callback": self._install,
                    "args": (preset,),
                },
            ],
        )

    async def aiogram_watcher(self, message: BotInlineMessage):
        if message.text != "/presets" or message.from_user.id != self._client.tg_id:
            return

        await self._menu()

    @loader.command()
    async def presets(self, message: Message):
        await self.inline.form(
            message=message,
            photo='https://imgur.com/a/Z6PP9as.png',
            text=self.strings('welcome').replace('/presets', self.get_prefix() + 'presets'),
            reply_markup=self._markup,
        )
