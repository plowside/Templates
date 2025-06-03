# -*- coding: utf- 8 -*-
from typing import Union

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database import *
from utils.functions import *
from data.config import *


################################################################################
#################################### ПРОЧЕЕ ####################################
# Кнопка "Назад"
def kb_back(data: str = 'admin:menu', text: str = '↪ Назад') -> InlineKeyboardMarkup:
	keyboard = ikb_construct(back_button=ikb(text, data=data))
	return keyboard.as_markup()

# Кнопка "Закрыть"
def kb_close(text: str = '❌ Закрыть') -> InlineKeyboardMarkup:
	keyboard = ikb_construct(back_button=ikb(text, data='utils:delete'))
	return keyboard.as_markup()



# Меню админа
def kb_admin_menu(admin_tg_user_id: int) -> InlineKeyboardMarkup:
	keyboard = ikb_construct(
		[ikb('🔍 Найти пользователя', data='admin:search')],
		back_button=ikb('❌ Закрыть', data='utils:delete')
	)
	return keyboard.as_markup()


# Поиск пользователя
def kb_admin_search() -> InlineKeyboardMarkup:
	keyboard = ikb_construct(
		back_button=ikb('↪ Назад', data='admin:menu')
	)
	return keyboard.as_markup()

# Меню найденного пользователя
def kb_admin_user(admin_tg_user_id: int, user_id: int) -> InlineKeyboardMarkup:
	keyboard = ikb_construct(
		[],
		back_button=ikb('↪ Назад', data='admin:menu')
	)
	return keyboard.as_markup()