# -*- coding: utf- 8 -*-
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.functions import *
from data.config import admin_ids


# Кнопки главного меню
def kb_main_menu(user_id) -> ReplyKeyboardMarkup:
	keyboard = rkb_construct(
		[rkb('🔥 Test')],
		[rkb('ℹ️ Информация')]
	)
	
	if user_id in [*admin_ids]:
		keyboard = rkb_construct([rkb('🧑🏻‍💻 Админ меню')], keyboard=keyboard)

	return keyboard.as_markup(resize_keyboard=True)