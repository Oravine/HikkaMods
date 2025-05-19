# https://github.com/Oravine/HikkaMods

# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# https://www.gnu.org/licenses/agpl-3.0.html

#Created by Telegram user: @Oravine
#Hikka Module


#╭━━━╮
#┃╭━╮┃
#┃┃╱┃┃╭━╮╭━━┳╮╭╮╭╮╭━╮╱╭━━╮
#┃┃╱┃┃┃╭╯┃╭╮┃╰╯┃┣┫┃╭╮╮┃┃━┫
#┃╰━╯┃┃┃╱┃╭╮┣╮╭╯┃┃┃┃┃┃┃┃━┫
#╰━━━╯╰╯╱╰╯╰╯╰╯╱╰╯╰╯╰╯╰━━╯

import asyncio
from hikkatl.types import Message
from hikkatl.tl.functions.messages import GetBotCallbackAnswerRequest
from hikkatl.tl.types import KeyboardButtonCallback

from .. import loader, utils

@loader.tds
class EVOAutoDrill(loader.Module):
    """Автоматическая заправка автобура в боте @MineEVO

Разработано: @OravineMods"""

#meta developer: @OravineMods
    
    strings = {
        "name": "EVOAutoDrill",
        "afon": "🟢 Автозаправка включена.\nЗаправка каждые <code>{}</code> часов",
        "afoff": "🔴 Автозаправка выключена",
        "af_already_on": "ℹ️ Автозаправка уже включена",
        "af_already_off": "ℹ️ Автозаправка уже выключена",
        "refueling": "⛽ Производится заправка автобура...",
        "refueled": "✅ Автобур заправлен",
        "config_delay": "Задержка между заправками (в часах)",
        "oneset_done": "✅ Единоразовая заправка выполнена",
        "adcfg_usage": "❌ Используйте:\n <code>adcfg <задержка в часах></code>",
        "adcfg_success": "✅ Задержка изменена на <code>{}</code> часов",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "delay",
                6,
                lambda: self.strings("config_delay"),
                validator=loader.validators.Integer(minimum=1)
            )
        )
        self._task = None

    async def client_ready(self, client, db):
        self._client = client
        self._db = db
        self._mineevo_bot = "@mineevo"

    async def _refuel(self):
        try:
            async with self._client.conversation(self._mineevo_bot) as conv:
                await conv.send_message("аб")
                response = await conv.get_response()

                # Ищем кнопку "Заправить" (2я в первой строке)
                if hasattr(response, "reply_markup") and response.reply_markup:
                    rows = response.reply_markup.rows
                    if len(rows) >= 1 and len(rows[0].buttons) >= 2:
                        button = rows[0].buttons[1]
                        if isinstance(button, KeyboardButtonCallback):
                            await self._client(GetBotCallbackAnswerRequest(
                                peer=self._mineevo_bot,
                                msg_id=response.id,
                                data=button.data
                            ))
                            return True
        except Exception as e:
            self.logger.error(f"Ошибка при заправке: {e}")
        return False

    async def _refuel_task(self):
        while True:
            try:
                await self._refuel()
                await asyncio.sleep(self.config["delay"] * 3600)
            except Exception as e:
                self.logger.error(f"Ошибка в задаче автозаправки: {e}")
                await asyncio.sleep(60)

    async def adoncmd(self, message: Message):
        """- 🟢 Включить автозаправку"""
        if self._task is not None and not self._task.done():
            await utils.answer(message, self.strings("af_already_on"))
            return

        self._task = asyncio.ensure_future(self._refuel_task())
        await utils.answer(message, self.strings("afon").format(self.config["delay"]))

    async def adoffcmd(self, message: Message):
        """- 🔴 Выключить автозаправку"""
        if self._task is None or self._task.done():
            await utils.answer(message, self.strings("af_already_off"))
            return

        self._task.cancel()
        self._task = None
        await utils.answer(message, self.strings("afoff"))

    async def adonecmd(self, message: Message):
        """- 🛢️ Выполнить единоразовую заправку"""
        await utils.answer(message, self.strings("refueling"))
        success = await self._refuel()
        if success:
            await utils.answer(message, self.strings("oneset_done"))
        else:
            await utils.answer(message, "❌ Не удалось выполнить заправку")

    async def adcfgcmd(self, message: Message):
        """<часы> - ⏱️ Изменить задержку между заправками"""
        args = utils.get_args_raw(message)
        if not args or not args.isdigit():
            await utils.answer(message, self.strings("adcfg_usage"))
            return

        delay = int(args)
        if delay < 1:
            await utils.answer(message, self.strings("adcfg_usage"))
            return

        self.config["delay"] = delay
        await utils.answer(message, self.strings("adcfg_success").format(delay))
