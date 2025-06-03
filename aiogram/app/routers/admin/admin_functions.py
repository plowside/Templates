# -*- coding: utf- 8 -*-
import asyncio, random, json

from datetime import datetime
from aiogram import Router, Bot, F
from aiogram.filters import Command, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from loader import dp, custom_fsm
from data.config import *
from database import *
from utils.functions import *
from keyboards import *
from .. import main_start

router = Router(name=__name__)





################################################################################
################################### MESSAGE ####################################

@router.callback_query(F.data.startswith('admin'))
async def callback_admin(call: CallbackQuery, bot: Bot, state: FSMContext, custom_data: str = None):
	cd = custom_data.split(':') if custom_data else call.data.split(':')
	tg_user_id, username, firstname = get_user(call)

	if cd[1] == 'menu':
		await call.message.edit_text('🧑🏻‍💻 Админ меню', reply_markup=kb_admin_menu(tg_user_id))

	elif cd[1] == 'search':
		if len(cd) == 2:
			await state.set_state('input_user_search')
			msg = await call.message.edit_text('<b>👤 Поиск пользователя</b>\n<i>Введите  <b>tg_id\\username</b>  пользователя</i>', reply_markup=kb_admin_search())
			await state.update_data(msg=msg)
		else:
			user_id = int(cd[2])
			user = await Userx.get(id=user_id)
			if not user:
				await call.answer('❌ Не удалось найти пользователя', show_alert=True)
				return

			reg_date = datetime.fromtimestamp(user.created_at).strftime("%d.%m.%Y")
			await call.message.edit_text(f'<b>Информация о пользователе</b>\n├ Юзернейм: {user_format_url(user)}\n├ ID телеграма:  <code>{user.tg_user_id}</code>\n└ Дата регистрации:  <code>{reg_date}</code>', reply_markup=kb_admin_user(tg_user_id, user.id))



@router.message(StateFilter('input_user_search'))
async def input_user_search(message: Message, bot: Bot, state: FSMContext):
	tg_user_id, username, firstname = get_user(message)
	mt = message.text.strip().replace('@', '')
	state_data = await state.get_data()
	await del_message(message, state_data.get('msg', None))
	if mt.isnumeric():
		mt = int(mt)
		user = await Userx.get(tg_user_id=mt, any_value=True)
	else:
		user = await Userx.get(tg_username=mt)

	if not user:
		msg = await message.answer('<b>❌ Не удалось найти пользователя</b>', reply_markup=kb_admin_search())
		await state.update_data(msg=msg)
		return
	await state.clear()

	reg_date = datetime.fromtimestamp(user.created_at).strftime("%d.%m.%Y")
	await message.answer(f'<b>Информация о пользователе</b>\n├ Юзернейм: {user_format_url(user)}\n├ ID телеграма:  <code>{user.tg_user_id}</code>\n└ Дата регистрации:  <code>{reg_date}</code>', reply_markup=kb_admin_user(tg_user_id, user.id))