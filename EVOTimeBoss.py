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

from hikkatl.types import Message
from hikka import loader, utils
import re
import asyncio
from datetime import timedelta

@loader.tds
class EVOTimeBoss(loader.Module):
    """Напоминает о появлении боссов в боте @MineEVO.

Разработчик: @OravineMods"""
    
#meta developer: @OravineMods
    
    strings = {
        "name": "EVOTimeBoss",
        "active": "🔔 Напоминания о боссах включены",
        "inactive": "🔕 Напоминания о боссах выключены",
        "already_active": "⚠️ Напоминания уже включены",
        "already_inactive": "⚠️ Напоминания уже выключены",
    }

    def __init__(self):
        self.active = False
        self.task = None
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "reminder_time",
                120,
                "За сколько секунд предупреждать о боссе",
                validator=loader.validators.Integer(minimum=10, maximum=300)),
        loader.ConfigValue(
                "chat_id_send",
                "me",
                "В какой чат отправить сотбщение. Чтобы отправть в избранное - «me»"
        ),
        loader.ConfigValue(
                "check_time",
                60,
                "Как часто проверять таймер боссов",
                validator=loader.validators.Integer(minimum=10, maximum=300))
        )

    async def client_ready(self, client, db):
        self._client = client

    async def parse_boss_time(self, time_str: str) -> int:
        """Парсит строку времени в секунды"""
        if time_str == "Жив!":
            return -1

        total_seconds = 0
        time_parts = {
            "ч.": 3600,
            "м.": 60,
            "с.": 1
        }

        for part, multiplier in time_parts.items():
            match = re.search(rf"(\d+)\s*{re.escape(part)}", time_str)
            if match:
                total_seconds += int(match.group(1)) * multiplier

        return total_seconds

    async def get_upcoming_bosses(self):
        """Получает список боссов, которые появятся менее чем через 2 минуты"""
        try:
            async with self._client.conversation("@mineevo") as conv:
                await conv.send_message("мбл")
                response = await conv.get_response()
                
                upcoming_bosses = []
                for line in response.text.split('\n'):
                    if not line.strip() or "Список таймеров боссов" in line:
                        continue
                    
                    # Убираем номер, эмодзи и теги в квадратных скобках
                    cleaned_line = re.sub(r"^\s*\d+\s*[⏳⚠️🚩]*\s*(\[[^\]]+\]\s*)?", "", line)
                    
                    # Разделяем на название босса и время
                    parts = cleaned_line.split("–", 1)
                    if len(parts) != 2:
                        continue
                    
                    boss_name = parts[0].strip()
                    time_str = parts[1].strip()
                    
                    time_seconds = await self.parse_boss_time(time_str)
                    if time_seconds == -1:
                        continue
                    
                    if 0 < time_seconds <= self.config["reminder_time"]:
                        upcoming_bosses.append(boss_name)
                
                return upcoming_bosses
        except Exception as e:
            print(f"Ошибка при получении боссов: {e}")
            return []

    async def check_bosses_loop(self):
        """Цикл проверки боссов"""
        while self.active:
            try:
                upcoming_bosses = await self.get_upcoming_bosses()
                if upcoming_bosses:
                    bosses_list = ", ".join(upcoming_bosses)
                    await self._client.send_message(
                        self.config["chat_id_send"],
                        f"<b>Скоро появятся босс(-ы):</b>\n<blockquote>{bosses_list}</blockquote>"
                    )
            except Exception as e:
                print(f"Ошибка в цикле проверки: {e}")
            
            await asyncio.sleep(self.config["check_time"])

    @loader.command()
    async def tbon(self, message: Message):
        """Включить напоминания о боссах"""
        if self.active:
            await utils.answer(message, self.strings("already_active"))
            return
        
        self.active = True
        self.task = asyncio.create_task(self.check_bosses_loop())
        await utils.answer(message, self.strings("active"))

    @loader.command()
    async def tboff(self, message: Message):
        """Выключить напоминания о боссах"""
        if not self.active:
            await utils.answer(message, self.strings("already_inactive"))
            return
        
        self.active = False
        if self.task:
            self.task.cancel()
            self.task = None
        await utils.answer(message, self.strings("inactive"))

    async def on_unload(self):
        if self.active and self.task:
            self.active = False
            self.task.cancel()