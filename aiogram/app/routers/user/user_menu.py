# -*- coding: utf- 8 -*-
import asyncio, json, ast

from datetime import datetime
from aiogram import Router, Bot, F
from aiogram.filters import Command, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from data.config import *
from database import *
from utils.functions import *
from keyboards import *
from .. import main_start

router = Router(name=__name__)






################################################################################
################################### MESSAGE ####################################

# Сделать test
@router.message(F.text == '🔥 Test')
async def create_test(message: Message, bot: Bot, state: FSMContext):
	await state.clear()
	await message.answer('<b>🔥 Test</b>\n└ test: <code>test</code>\n\n<i>♦️ Выберите один из предложенных вариантов.</i>', reply_markup=kb_test())

@router.callback_query(F.data.startswith('testing'))
async def callback_testing(call: CallbackQuery, bot: Bot, state: FSMContext, custom_data: str = None):
	cd = custom_data.split(':') if custom_data else call.data.split(':')
	req_type = cd[1]

	if cd[2] == 'test': # Test обычный
		await call.message.edit_text(f'Test test passed', reply_markup=kb_back())

	if cd[2] == 'test': # Test state
		ts = datetime.now()
		msg = await call.message.edit_text(f'Test state started, value = {ts}', reply_markup=kb_back())
		await state.set_state('input_test')

		await state.update_data(test_value=ts, msgs=[msg])



@router.message(StateFilter('input_test'))
async def input_test(message: Message, bot: Bot, state: FSMContext):
	tg_user_id, username, firstname = get_user(message)
	mt = message.text
	state_data = await state.get_data()


	await state.clear()
	await del_message(*state_data.get('msgs', []), message)
	await message.answer(f'test passed, value = {state_data.get("ts")}', reply_markup=kb_close())


@router.callback_query(StateFilter('input_req'))
async def input_req_(call: CallbackQuery, bot: Bot, state: FSMContext):
	tg_user_id, username, firstname = get_user(call)
	cd = call.data.split(':')
	state_data = await state.get_data()


	await state.clear()
	await call.message.edit_text(f'test passed, value = {state_data.get("ts")}', reply_markup=kb_close())




# Ответы на вопросы
@router.message(F.text == 'ℹ️ Информация')
async def faq(message: Message, bot: Bot, state: FSMContext):
	await state.clear()

	await message.answer('<b>💻 TEST INFORMATION.', disable_web_page_preview=True, reply_markup=kb_info())