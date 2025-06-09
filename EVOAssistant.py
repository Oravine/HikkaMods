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
	"""Модуль ассистент для бота @Mine_EVO_Bot. В этом модуле содержится много полезной информации по этому боту.
	
Разработчик: @OravineMods"""
	
#meta developer: @OravineMods
	version = (4_0_0)
		
	strings = {
		'name': 'EVOAssistant',
		'menu': '<b>🏠 Главное меню</b>\n\nНажмите <i>💸 Сокращения денег</i>, чтобы посмотреть сокращения денег.\nНажмите <i>🎈 Список ивентов</i>, чтобы посмотреть список всех ивентов .Нажмите <i>🏰 Кланы</i>, чтобы посмотреть информацию о кланах. \n\n<blockquote><i>Разработанно: @OravineMods</i></blockquote>',
		'list': '<b>💸 Список сокращений денег</b>\n\nНа кнопках в столбик написаны сокращения. Они идут от меньшего к большему, по столбцам, т. е. сверху вниз, слева направо.',
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
			reply_markup=[[{'text': '💸 Сокращения денег', 'callback': self.mlist}],[{'text': '🎈 Список ивентов', 'callback': self.evlist}],[{'text': '🏰 Кланы', 'callback': self.clmenu}],[{'text': '⛔ Запрещенные модули', 'callback': self.zmmenu}],[{'text': '❌ Закрыть', "action": "close"}]])
			
	@loader.command()
	async def eamenu(self, message):
		"""- 🏠 Открывает главное меню"""
		await self.inline.form(
			message=message,
			text = self.strings['menu'],
			reply_markup=[[{'text': '💸 Сокращения денег', 'callback': self.mlist}],[{'text': '🎈 Список ивентов', 'callback': self.evlist}],[{'text': '🏰 Кланы', 'callback': self.clmenu}],[{'text': '⛔ Запрещенные модули', 'callback': self.zmmenu}],[{'text': '❌ Закрыть', "action": "close"}]])
	
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
			
			#Раздел кланы начало
			
	cl = {
		'menu': '<b>🏰 Кланы</b>\n\nЗдесь есть информация о создании, прокачке и бонусах клана. Выберите нужный раздел.',
		'lvlmenu': '<b>🏰 Кланы</b>\n\nЗдесь есть информация об уровнях клана. Выберите нужный уровень.',
		'cr': '<b>🏰 Создать клан</b>\n\n<blockquote><b>Стоимость создания:</b>\n<i>⭐ Уровень:</i> <code>50</code>\n<i>🎆 Плазма:</i> <code>25,000</code></blockquote>',
		'lvl1': '<b>Уровень:</b> <code>1</code>\n<b>Иконка:</b> <code>⛺</code>\n<b>Стоимость прокачки:</b>\n<i>Нет</i>\n<b>Бонусы:</b>\n<blockquote><i>🔥 Множ. руды:</i> <code>×1.25</code>\n<i>☘ Шк:</i> <code>+0.1</code>\n<i>🚩 Макс. боссов:</i> <code>0</code>\n<i>🛡 Щит:</i> <code>Нет</code>\n<i>👥 Участники:</i> <code>10</code></blockquote>',
		'lvl2': '<b>Уровень:</b> <code>2</code>\n<b>Иконка:</b> <code>🛖</code>\n<b>Стоимость прокачки:</b>\n<blockquote><i>🎆 Плазма:</i> <code>1,500,000</code>\n<i>📜 Эскиз:</i> <code>100</code>\n<i>🏅 Очки клана: </i><code>500</code></blockquote>\n<b>Бонусы:</b>\n<blockquote><i>🔥 Множ. руды:</i> <code>×1.5</code>\n<i>☘ Шк:</i> <code>+0.2</code>\n<i>🚩 Макс. боссов:</i> <code>1</code>\n<i>🛡 Щит:</i> <code>1 день</code>\n<i>👥 Участники:</i> <code>20</code></blockquote>',
		'lvl3': '<b>Уровень:</b> <code>3</code>\n<b>Иконка:</b> <code>🏠</code>\n<b>Стоимость прокачки:</b>\n<blockquote><i>🎆 Плазма:</i> <code>5,000,000</code>\n<i>📜 Эскиз:</i> <code>500</code>\n<i>🔩 Скрап:</i> <code>150</code>\n<i>🏅 Очки клана: </i><code>2,500</code></blockquote>\n<b>Бонусы:</b>\n<blockquote><i>🔥 Множ. руды:</i> <code>×1.75</code>\n<i>☘ Шк:</i> <code>+0.3</code>\n<i>🚩 Макс. боссов:</i> <code>2</code>\n<i>🛡 Щит:</i> <code>1 день</code>\n<i>👥 Участники:</i> <code>30</code></blockquote>',
		'lvl4': '<b>Уровень:</b> <code>4</code>\n<b>Иконка:</b> <code>🏘</code>\n<b>Стоимость прокачки:</b>\n<blockquote><i>🎆 Плазма:</i> <code>15,000,000</code>\n<i>📜 Эскиз:</i> <code>1,500</code>\n<i>🌀 Эссенсия:</i> <code>150</code>\n<i>🔩 Скрап:</i> <code>1,200</code>\n<i>🏅 Очки клана: </i><code>12,500</code></blockquote>\n<b>Бонусы:</b>\n<blockquote><i>🔥 Множ. руды:</i> <code>×2</code>\n<i>☘ Шк:</i> <code>+0.4</code>\n<i>🚩 Макс. боссов:</i> <code>2</code>\n<i>🛡 Щит:</i> <code>2 дня</code>\n<i>👥 Участники:</i> <code>40</code></blockquote>',
		'lvl5': '<b>Уровень:</b> <code>5</code>\n<b>Иконка:</b> <code>🏰</code>\n<b>Стоимость прокачки:</b>\n<blockquote><i>🎆 Плазма:</i> <code>30,000,000</code>\n<i>📜 Эскиз:</i> <code>4,500</code>\n<i>🌀 Эссенсия:</i> <code>600</code>\n<i>🔩 Скрап:</i> <code>9,600</code>\n<i>🌌 Зв. пыль:</i> <code>5</code>\n<i>🏅 Очки клана: </i><code>50,000</code></blockquote>\n<b>Бонусы:</b>\n<blockquote><i>🔥 Множ. руды:</i> <code>×3</code>\n<i>☘ Шк:</i> <code>+0.5</code>\n<i>🚩 Макс. боссов:</i> <code>3</code>\n<i>🛡 Щит:</i> <code>2 дня</code>\n<i>👥 Участники:</i> <code>50</code></blockquote>',
		'lvl6': '<b>Уровень:</b> <code>6</code>\n<b>Иконка:</b> <code>🏯</code>\n<b>Стоимость прокачки:</b>\n<blockquote><i>🎆 Плазма:</i> <code>100,000,000</code>\n<i>🌌 Зв. пыль:</i> <code>30</code>\n<i>🏅 Очки клана: </i><code>100,000</code></blockquote>\n<b>Бонусы:</b>\n<blockquote><i>🔥 Множ. руды:</i> <code>×4</code>\n<i>☘ Шк:</i> <code>+0.55</code>\n<i>🚩 Макс. боссов:</i> <code>3</code>\n<i>🛡 Щит:</i> <code>3 дня</code>\n<i>👥 Участники:</i> <code>55</code></blockquote>'
	}
	
	async def clmenu(self, call):
		await call.edit(
			text = self.cl['menu'],
			reply_markup=[[{'text': 'Создание клана', 'callback': self.cr},{'text': 'Уровни клана', 'callback': self.lvlmenu}],[{'text': '🔙 В меню', 'callback': self.menu},{'text': '❌ Закрыть', 'action': 'close'}]])
			
	async def lvlmenu(self, call):
		await call.edit(
			text = self.cl['lvlmenu'],
			reply_markup=[[{'text': '1', 'callback': self.lvl1},{'text': '2', 'callback': self.lvl2},{'text': '3', 'callback': self.lvl3},{'text': '4', 'callback': self.lvl4},{'text': '5', 'callback': self.lvl5},{'text': '6', 'callback': self.lvl6}],[{'text': '🔙 Назад', 'callback': self.clmenu}]])
			
	async def cr(self, call):
		await call.edit(
			text = self.cl['cr'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.clmenu}])
	
	async def lvl1(self, call):
		await call.edit(
			text = self.cl['lvl1'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.lvlmenu}])
			
	async def lvl2(self, call):
		await call.edit(
			text = self.cl['lvl2'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.lvlmenu}])
			
	async def lvl3(self, call):
		await call.edit(
			text = self.cl['lvl3'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.lvlmenu}])
			
	async def lvl4(self, call):
		await call.edit(
			text = self.cl['lvl4'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.lvlmenu}])
			
	async def lvl5(self, call):
		await call.edit(
			text = self.cl['lvl5'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.lvlmenu}])
			
	async def lvl6(self, call):
		await call.edit(
			text = self.cl['lvl6'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.lvlmenu}])
	
			#Раздел кланы конец
			
			#Раздел правила начало
			
	rul = {
		'Note': 'Не забить на это',
		'Real': 'Забил'#Когда нибудь сделаю
	}						#но не сейчас
			
			#Раздел правила конец
			
			#Раздел модули начало
			
	zm = {
		'menu': '⛔️ <b>Список запрещённых модулей</b>\n\nНа кнопках ниже список запрещённых модулей. Нажмите на кнопку чтобы узнать подробности. Если рядом с названием стоит знак «❕», то значит этот модуль не запрещён, но его использование ограничено.\n\n<blockquote><i>Справка: модуль - код для юзерботов (в данном случае Hikka/Heroku), который загружается отдельно и помогает выполнять действия от имени пользователя.</i></blockquote>',
		'tb': '<b>Модуль:</b> <code>Уведомления о боссах</code>\n\n<b>Описание:</b> <i>Предупреждает пользователя о появлении босса, отправляя сообщение.(Работает через команду Мбл)</i>\n\n<b>Примечание:</b> <i>Модуль разрешён только если уведомление отправляется в личный чат пользователя без других людей, если сообщение отправляется в чат с другими людьми, то модуль запрщен.</i>',
		'ab': '<b>Модуль:</b> <code>Авто выбор боссов</code>\n\n<b>Описание:</b> <i>Автоматически выбирает босса, который жив и атакует его. </i>\n\n<b>Примечание:</b> <i>По информации от создателя бота, умная автоатака разрешена, т. е. модуль который бьет босса пока у вас не останется N здоровья разрешён, но только если он активируется в ручную на одного босса.</i>',
		'at': '<b>Модуль:</b> <code>Автопринятие трейдов</code>\n\n<b>Описание:</b> <i>Автоматически принимает трейд. В любом виде. </i>\n\n<b>Примечание:</b> <i>Нет.</i>'
	}
	
	async def zmmenu(self, call):
		await call.edit(
			text = self.zm['menu'],
			reply_markup=[[{'text': '❕ Уведомления о боссах', 'callback': self.tb}],[{'text': '❕ Авто выбор боссов', 'callback': self.ab}],[{'text': 'Автопринятие трейдов', 'callback': self.at}],[{'text': '🔙 Назад', 'callback': self.menu},{'text': '❌ Закрыть', 'action': 'close'}]])
			
	async def tb(self, call):
		await call.edit(
			text = self.zm['tb'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.zmmenu}])
			
	async def ab(self, call):
		await call.edit(
			text = self.zm['ab'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.zmmenu}])
			
	async def at(self, call):
		await call.edit(
			text = self.zm['at'],
			reply_markup=[{'text': '🔙 Назад', 'callback': self.zmmenu}])
			
			#Раздел модули конец
