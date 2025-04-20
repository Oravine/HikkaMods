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


from .. import loader, utils
from ..inline.types import InlineCall
@loader.tds
class LoadHelper(loader.Module):
	"""Помощь для скачивания юзербота Hikka. Есть несколько вариантов скачивания."""
	
	strings = {
		'name': 'LoadHelper',
		'nt1': '<b>1. Чтобы скачать Hikka через Termux нужен сам Termux. Для этого скачиваем его <a href="https://f-droid.org/repo/com.termux_118.apk">по ссылке</a>. Если уже установлен Teremux, лучше удалить его и скачать заново по ссылке.\n<i>⚠ Версия из Play Market не подойдёт!</i></b>',
		'nt2': '<b>2. Введите в терминал Termux команду:\n<code>termux-wake-lock && export AIOHTTP_NO_EXTENSIONS=1 && pkg upgr -y && pkg i wget ncurses-utils python openssl git -y && clear && . &lt;(wget -qO- https://raw.githubusercontent.com/hikariatama/Hikka/refs/heads/master/termux.sh)</code></b>',
		'nt3': '<b>3. На все что спрашивает скрипт отвечайте «<code>y</code>».</b>',
		'nt4': '<b>4. Следуйте инструкциям в скрипте. Когда попросят нужно будет ввести <i>API_ID</i> и <i>API_HASH</i>. Чтобы узнать как их получить, <a href="https://youtu.be/DcqDA249Lhg?t=24">посмотрите видео</a>. Далее следуйте инструкции в скрипте.</b>',
		'nt5': '<b>5. Все готово! Если у вас остались вопросы, вы можете написать в официальный <a href="https://t.me/hikka_talks">чат поддержки</a> Hikka.</b>'
		}

#meta developer: @OravineMods

	version = (1_0_0)
	
	async def tmn1(self, call):
		await call.edit(
			text = self.strings['nt1'],
			reply_markup=[{'text': 'Далее', 'callback': self.tmn2},{'text': 'Закрыть', "action": "close"}])
			
	async def tmn2(self, call):
		await call.edit(
			text = self.strings['nt2'],
			reply_markup=[{'text': 'Далее', 'callback': self.tmn3},{'text': 'Назад', 'callback': self.tmn1}])
			
	async def tmn3(self, call):
		await call.edit(
			text = self.strings['nt3'],
			reply_markup=[{'text': 'Далее', 'callback': self.tmn4},{'text': 'Назад', 'callback': self.tmn2}])
			
	async def tmn4(self, call):
		await call.edit(
			text = self.strings['nt4'],
			reply_markup=[{'text': 'Далее', 'callback': self.tmn5},{'text': 'Назад', 'callback': self.tmn3}])
			
	async def tmn5(self, call):
		await call.edit(
			text = self.strings['nt5'],
			reply_markup=[{'text': 'Назад', 'callback': self.tmn4},{'text': 'Чат Hikka', 'url': 'https://t.me/hikka_talks'}])
				
	@loader.command()
	async def teremux_guide(self, message):
		"""Гайд бесплатной установки на Termux"""
		await self.inline.form(
			message=message,
			text = self.strings['nt1'],
			reply_markup=[{'text': 'Далее', 'callback': self.tmn2},{'text': 'Закрыть', "action": "close"}])
