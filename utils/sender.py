from aiogram.types import InputFile
async def send_pdf(user_id, bot):
 await bot.send_document(user_id, InputFile('assets/gift.pdf'), caption='🎁 Лови подарок!')