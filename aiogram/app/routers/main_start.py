# -*- coding: utf- 8 -*-
from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


from data.config import *
from keyboards.reply_main import *

router = Router(name=__name__)


################################################################################
#################################### ПРОЧЕЕ ####################################
# Открытие главного меню
@router.message(F.text.in_('/start'))
async def main_start(message: Message, bot: Bot, state: FSMContext):
	await state.clear()

	await message.answer(f'''
<b>💬 Добро пожаловать в test bot!</b>

<i>❕ Продолжая пользоваться ботом, Вы соглашаетесь с <a href="https://telegra.ph/User-agreement-08-31-36">условиями использования сервиса</a></i>
''', reply_markup=kb_main_menu(message.from_user.id), disable_web_page_preview=True)



@router.callback_query(F.data.startswith('utils'))
async def utils(call: CallbackQuery, bot: Bot, state: FSMContext, custom_state: str = None):
	cd = custom_state.split(':') if custom_state else call.data.split(':')

	if cd[1] == 'delete':
		await del_message(call.message)

	elif cd[1] == 'menu':
		if cd[2] == 'main':
			await del_message(call.message)
			await call.message.answer(f'''
<b>💬 Добро пожаловать в test bot!</b>

<i>❕ Продолжая пользоваться ботом, Вы соглашаетесь с <a href="https://telegra.ph/User-agreement-08-31-36">условиями использования сервиса</a></i>
''', reply_markup=kb_main_menu(call.from_user.id), disable_web_page_preview=True)

# @router.callback_query(F.data.startswith('missed'))
# async def utils(call: CallbackQuery, bot: Bot, state: FSMContext, custom_state: str = None):
# 	await del_message(call.message)