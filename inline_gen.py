from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from msg_gen import *

bio_btn = InlineKeyboardButton(Texts.bio_button_text, callback_data = 'bio_state_message')
about_btn = InlineKeyboardButton(Texts.about_project_button_text, callback_data = 'about_state_message')
all_projects_btn = InlineKeyboardButton(Texts.all_projects_button_text, callback_data = 'all_projects_state_message')
back_btn = InlineKeyboardButton(Texts.back_button_text, callback_data = 'btn_back')


# inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3, inline_btn_2, inline_btn_1)

def gen_inl_kb(back = False, start = False, state = None, prev_state = None, projects = None):
	inline_kb = InlineKeyboardMarkup(row_width = 1)
	if start or (state == 'start_state_message'):
		inline_kb.add(bio_btn, about_btn, all_projects_btn)
	elif projects:
		for text in Texts.projects_button_text:
			prj_btn = InlineKeyboardButton(text, callback_data = f'{text}')
			inline_kb.add(prj_btn)
	if back:
		back_btn = InlineKeyboardButton(Texts.back_button_text, callback_data = prev_state)
		inline_kb.add(back_btn)
	return inline_kb
