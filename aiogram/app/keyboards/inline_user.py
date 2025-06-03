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
def kb_back(data: str = 'user:menu', text: str = '↪ Назад') -> InlineKeyboardMarkup:
	keyboard = ikb_construct(back_button=ikb(text, data=data))
	return keyboard.as_markup()

# Кнопка "Закрыть"
def kb_close(text: str = '❌ Закрыть') -> InlineKeyboardMarkup:
	keyboard = ikb_construct(back_button=ikb(text, data='utils:delete'))
	return keyboard.as_markup()



def kb_test():
	keyboard = ikb_construct(
		[ikb('⚙️ Test', data='testing:test:test'), ikb('⚙️ Test state', data='testing:test:state')],
		back_button=ikb('❌ Закрыть', data='utils:delete')
	)
	return keyboard.as_markup()



# Информация
def kb_info() -> InlineKeyboardMarkup:
	keyboard = ikb_construct(
		[ikb('📍 Администратор', url=url_administrator)],
		back_button=ikb('❌ Закрыть', data='utils:delete')
	)
	return keyboard.as_markup()
################################################################################
################################### ПЛАТЕЖИ ####################################