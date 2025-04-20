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
@loader.tds
class Smile(loader.Module):
	"""Отправляет разные смайлики из символов. Разработано: @Oravine.
version.1.0"""
	strings = {'name': 'Smile'}

#meta developer: @OravineMods

	version = (1_0_0)

	@loader.command()
	async def sml1(self, message):
		"""Пишет -_-"""
		await message.edit("-_-")
		
	@loader.command()
	async def sml2(self, message):
		"""Пишет :)"""
		await message.edit(":)")
		
	@loader.command()
	async def sml3(self, message):
		"""Пишет :("""
		await message.edit(":(")
		
	@loader.command()
	async def sml4(self, message):
		"""Пишет ¯\_(ツ)_/¯"""
		await message.edit("¯\_(ツ)_/¯")
		
	@loader.command()
	async def sml5(self, message):
		"""Пишет (˶ᵔ ᵕ ᵔ˶)"""
		await message.edit("(˶ᵔ ᵕ ᵔ˶)")
		
	@loader.command()
	async def sml6(self, message):
		"""Пишет ≽^•⩊•^≼"""
		await message.edit("≽^•⩊•^≼")
		
	@loader.command()
	async def sml7(self, message):
		"""Пишет ( ° ʖ °)"""
		await message.edit("( ° ʖ °)")
		
	@loader.command()
	async def sml8(self, message):
		"""Пишет *амогус ебет чела*"""
		await message.edit("𓀐𓂸ඞ")
		
	@loader.command()
	async def sml9(self, message):
		"""Пишет ╭∩╮( •̀_•́ )╭∩╮"""
		await message.edit("╭∩╮( •̀_•́ )╭∩╮")
		
	@loader.command()
	async def sml10(self, message):
		"""Пишет ʕ⁠っ⁠•⁠ᴥ⁠•⁠ʔ⁠っ"""
		await message.edit("ʕ⁠っ⁠•⁠ᴥ⁠•⁠ʔ⁠っ")
		
	@loader.command()
	async def sml11(self, message):
		"""Пишет *недовольный котик*"""
		await message.edit(" /⁠ᐠ⁠｡⁠ꞈ⁠｡⁠ᐟ⁠\ ")
		
	@loader.command()
	async def sml12(self, message):
		"""Пишет *радостный смайлик*"""
		await message.edit("\(⁠^⁠o⁠^⁠)⁠/")
		
	@loader.command()
	async def sml13(self, message):
		"""Пишет *удивленный смайлик*"""
		await message.edit("⊙⁠.⁠☉")
		
	@loader.command()
	async def sml14(self, message):
		"""Пишет *печальный смайлик*"""
		await message.edit("(⁠˘⁠･⁠_⁠･⁠˘⁠)")
