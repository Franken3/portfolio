from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from inline_gen import gen_inl_kb
from msg_gen import *

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


# bot.py
@dp.message_handler(commands = ['start'])
async def process_command(message: types.Message):
	await bot.delete_message(message.from_user.id, message_id = message.message_id)
	await bot.send_message(message.from_user.id, text = Texts.start_state_text, reply_markup = gen_inl_kb(start = True))


@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
	# Неприятное решение для переачи экхемпляров класса через тг апи для получения инфы о state
	callback_data = states[callback_query.data]
	back = False
	projects = False
	if callback_query.data != 'start_state_message':
		back = True
	if callback_query.data == 'all_projects_state_message':
		projects = True
	reply_markup = gen_inl_kb(back = back,
							  state = callback_query.data,
							  prev_state = callback_data.prev_state,
							  projects = projects)

	await bot.edit_message_text(text = callback_data.text_state,
								chat_id = callback_query.from_user.id,
								message_id = callback_query.message.message_id,
								reply_markup = reply_markup,
								parse_mode='html')


# Просто чистис все сообщения
@dp.message_handler()
async def del_spam(message: types.Message):
	await bot.delete_message(message.from_user.id, message_id = message.message_id)


if __name__ == '__main__':
	executor.start_polling(dp)
