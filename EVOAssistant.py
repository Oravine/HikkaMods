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
class EVOAssistant(loader.Module):
	"""Модуль ассистент для бота @Mine_EVO_Bot. В этом модуле содержится много полезной информации по этому боту."""
	
#meta developer: @OravineMods
	version = (2_0_0)
		
	strings = {
		'name': 'EVOAssistant',
		'menu': '<b>Главное меню</b>\n\nНажмите <i>Открыть список</i>, чтобы посмотреть сокращения денег.\n\n<blockquote><i>Разработанно: @OravineMods</i></blockquote>',
		'list': '<b>💸 Список сокращений денег</b>\nНа кнопках в столбик написаны сокращения. Они идут от меньшего к большему, по столбцам, т. е. сверху вниз, слева направо.',
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

			#Главное меню начало	
			
	async def menu(self, call):
		await call.edit(
			text = self.strings['menu'],
			reply_markup=[[{'text': '💸 Сокращения денег', 'callback': self.mlist}],[{'text': '🎈 Список ивентов', 'callback': self.evlist}],[{'text': '❌ Закрыть', "action": "close"}]])
			
	@loader.command()
	async def eamenu(self, message):
		"""- Открывает главное меню"""
		await self.inline.form(
			message=message,
			text = self.strings['menu'],
			reply_markup=[[{'text': '💸 Сокращения денег', 'callback': self.mlist}],[{'text': '🎈 Список ивентов', 'callback': self.evlist}],[{'text': '❌ Закрыть', "action": "close"}]])
	
			#Главное меню конец
			
			#Раздел деньги начало
			
	async def mlist(self, call):
		await call.edit(
			text = self.strings['list'],
			reply_markup=[[{'text': 'K', 'callback': self.K},{'text': 'Qa', 'callback': self.Qa},{'text': 'O', 'callback': self.O}],[{'text': 'M', 'callback': self.M},{'text': 'Qi', 'callback': self.Qi},{'text': 'N', 'callback': self.N}],[{'text': 'B', 'callback': self.B},{'text': 'Sx', 'callback': self.Sx},{'text': 'D', 'callback': self.D}],[{'text': 'T', 'callback': self.T},{'text': 'Sp', 'callback': self.Sp},{'text': 'Aa, Bb...', 'callback': self.Aa}],[{'text': '🔙 В меню', 'callback': self.menu},{'text': '❌ Закрыть', "action": "close"}]])
	
	async def K(self, call):
		await call.edit(
			text = self.strings['K'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def M(self, call):
		await call.edit(
			text = self.strings['M'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
	
	async def B(self, call):
		await call.edit(
			text = self.strings['B'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
	
	async def T(self, call):
		await call.edit(
			text = self.strings['T'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def Qa(self, call):
		await call.edit(
			text = self.strings['Qa'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
	
	async def Qi(self, call):
		await call.edit(
			text = self.strings['Qi'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def Sx(self, call):
		await call.edit(
			text = self.strings['Sx'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def Sp(self, call):
		await call.edit(
			text = self.strings['Sp'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def O(self, call):
		await call.edit(
			text = self.strings['O'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def N(self, call):
		await call.edit(
			text = self.strings['N'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def D(self, call):
		await call.edit(
			text = self.strings['D'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])
			
	async def Aa(self, call):
		await call.edit(
			text = self.strings['Aa'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.mlist}])

			#Раздел деньги конец
			
			#Раздел ивенты начало
			
	ev = {
		'list': '<b>🎈Список ивентов</b>\n\nНиже на кнопках указаны названия ивентов. Нажмите на него, чтобы посмотреть информацию о выбранном ивенте.',
		'plasm': '<b>🟣 Плазменный Шторм</b>\n\n🗓 День: <i>Вторник</i>\n\n⚡ Буст: <i>Шанс найти плазму +20%</i>',
		'boss': '<b>🟢 Босс Хант</b>\n\n🗓 День: <i>Среда</i>\n\n⚡ Бусты:\n<i>· Время появления боссов снижено в 2 раза\n· Здоровье боссов увеличено в 2 раза\n· Шанс получить уникальный дроп с босса +10%\n· Эликсир не работает</i>',
		'mine': '<b>🟠 Шахтёрская Лихорадка</b>\n\n🗓 День: <i>Пятница</i>\n\n⚡ Буст: <i>Добыча руды ×2 (действует на автобур)</i>',
		'case': '<b>🟤 Урожай Кейсов</b>\n\n🗓 День: <i>Суббота</i>\n\n⚡ Буст: <i>Шанс найти кейс +50%</i>',
		'gold': '<b>🟡 Золотой Бум</b>\n\n🗓 День: <i>Воскресенье</i>\n\n⚡ Буст: <i>Продажа руды ×3</i>'
	}
		
	async def evlist(self, call):
		await call.edit(
			text = self.ev['list'],
			reply_markup=[[{'text': '🟣 Плазменный Шторм', 'callback': self.plasm}],[{'text': '🟢 Босс Хант', 'callback': self.boss}],[{'text': '🟠 Шахтёрская Лихорадка', 'callback': self.mine}],[{'text': '🟤 Урожай Кейсов', 'callback': self.case}],[{'text': '🟡 Золотой Бум', 'callback': self.gold}],[{'text': '🔙 В меню', 'callback': self.menu},{'text': '❌ Закрыть', 'action': 'close'}]])
			
	async def plasm(self, call):
		await call.edit(
			text = self.ev['plasm'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.evlist}])
	
	async def boss(self, call):
		await call.edit(
			text = self.ev['boss'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.evlist}])
			
	async def mine(self, call):
		await call.edit(
			text = self.ev['mine'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.evlist}])
			
	async def case(self, call):
		await call.edit(
			text = self.ev['case'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.evlist}])
			
	async def gold(self, call):
		await call.edit(
			text = self.ev['gold'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.evlist}])
			
			#Раздел ивенты конец