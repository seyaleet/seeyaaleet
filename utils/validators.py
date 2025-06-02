from aiogram import Bot
from config import CHANNEL_ID
async def check_subscription(user_id):
 bot = Bot.get_current()
 member = await bot.get_chat_member(CHANNEL_ID, user_id)
 return member.status in ['member', 'creator', 'administrator']