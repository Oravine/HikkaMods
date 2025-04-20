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
class MoneyEVO(loader.Module):
	"""Модуль со списком условных обозначений чисел в боте @Mine_EVO_Bot."""
	
#meta developer: @OravineMods
	version = (1_0_0)
		
	strings = {
		'name': 'MoneyEVO',
		'menu': '<b>Главное меню</b>\n\nНажмите <i>Открыть список</i>, чтобы посмотреть сокращения денег.\n\n<blockquote><i>Разработанно: @OravineMods</i></blockquote>',
		'list': '<b>Список сокращений денег</b>\nНа кнопках в столбик написаны сокращения. Они идут от меньшего к большему, по столбцам, т. е. сверху вниз, слева направо.',
		'K': '<b>Сокращение: </b><code>K</code><b>\nСумма: </b><code>Тысяча</code>\n<b>Написание:</b> <code>K</code> / <code>к</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'M': '<b>Сокращение: </b><code>M</code><b>\nСумма: </b><code>Миллион</code>\n<b>Написание:</b> <code>M</code> / <code>м</code> / <code>кк</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'B': '<b>Сокращение: </b><code>B</code><b>\nСумма: </b><code>Миллиард</code><b>\nНаписание:</b> <code>B</code> / <code>б</code> / <code>ккк</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'T': '<b>Сокращение: </b><code>T</code><b>\nСумма: </b><code>Триллион</code><b>\nНаписание:</b> <code>T</code> / <code>т</code> / <code>кккк</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'Qa': '<b>Сокращение: </b><code>Qa</code><b>\nСумма: </b><code>Квадриллион</code><b>\nНаписание:</b> <code>Qa</code> / <code>кв</code> / <code>ква</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'Qi': '<b>Сокращение: </b><code>Qi</code><b>\nСумма: </b><code>Квинтиллион</code><b>\nНаписание:</b> <code>Qi</code> / <code>ки</code> / <code>кви</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'Sx': '<b>Сокращение: </b><code>Sx</code><b>\nСумма: </b><code>Секстиллион</code><b>\nНаписание:</b> <code>Sp</code> / <code>ск</code> / <code>сек</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'Sp': '<b>Сокращение: </b><code>Sp</code><b>\nСумма: </b><code>Септиллион</code><b>\nНаписание:</b> <code>Sp</code> / <code>сп</code> / <code>сеп</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'O': '<b>Сокращение: </b><code>O</code><b>\nСумма: </b><code>Октиллион</code><b>\nНаписание:</b> <code>O</code> / <code>о</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'N': '<b>Сокращение: </b><code>N</code><b>\nСумма: </b><code>Нониллион</code><b>\nНаписание:</b> <code>N</code> / <code>н</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'D': '<b>Сокращение: </b><code>D</code><b>\nСумма: </b><code>Дециллион</code><b>\nНаписание:</b> <code>D</code> / <code>д</code>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>',
		'Aa': '<b>Сокращение: </b><code>Aa</code>, <code>Bb</code>, <code>Cc</code> <i>и т. д.</i><b>\nСумма: </b><code>—</code><b>\nНаписание:</b> <code>Aa</code>, <code>Bb</code>, <code>Cc</code> <i>и т. д. </i>\n\n<i>Нажмите назад, чтобы вернуться к списку.</i>'
	}

	async def menu(self, call):
		await call.edit(
			text = self.strings['menu'],
			reply_markup=[{'text': 'Открыть список', 'callback': self.list},{'text': 'Закрыть', "action": "close"}])
			
	async def list(self, call):
		await call.edit(
			text = self.strings['list'],
			reply_markup=[[{'text': 'В меню', 'callback': self.menu},{'text': 'Закрыть', "action": "close"}],[{'text': 'K', 'callback': self.K},{'text': 'Qa', 'callback': self.Qa},{'text': 'O', 'callback': self.O}],[{'text': 'M', 'callback': self.M},{'text': 'Qi', 'callback': self.Qi},{'text': 'N', 'callback': self.N}],[{'text': 'B', 'callback': self.B},{'text': 'Sx', 'callback': self.Sx},{'text': 'D', 'callback': self.D}],[{'text': 'T', 'callback': self.T},{'text': 'Sp', 'callback': self.Sp},{'text': 'Aa, Bb...', 'callback': self.Aa}]])
	
	async def K(self, call):
		await call.edit(
			text = self.strings['K'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def M(self, call):
		await call.edit(
			text = self.strings['M'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
	
	async def B(self, call):
		await call.edit(
			text = self.strings['B'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
	
	async def T(self, call):
		await call.edit(
			text = self.strings['T'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def Qa(self, call):
		await call.edit(
			text = self.strings['Qa'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
	
	async def Qi(self, call):
		await call.edit(
			text = self.strings['Qi'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def Sx(self, call):
		await call.edit(
			text = self.strings['Sx'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def Sp(self, call):
		await call.edit(
			text = self.strings['Sp'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def O(self, call):
		await call.edit(
			text = self.strings['O'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def N(self, call):
		await call.edit(
			text = self.strings['N'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def D(self, call):
		await call.edit(
			text = self.strings['D'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	async def Aa(self, call):
		await call.edit(
			text = self.strings['Aa'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.list}])
			
	
	@loader.command()
	async def emmenu(self, message):
		"""Открывает главное меню"""
		await self.inline.form(
			message=message,
			text = self.strings['menu'],
			reply_markup=[{'text': 'Открыть список', 'callback': self.list},{'text': 'Закрыть', "action": "close"}])
			
	#Модуль не закончен
