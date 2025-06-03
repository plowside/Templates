# -*- coding: utf- 8 -*-
from aiogram import Router, Bot, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from database import *
from data.config import *
from loader import custom_fsm
from utils.functions import *

router = Router(name=__name__)


# Колбэк с обработкой кнопки
@router.callback_query(F.data == '...')
async def main_missed_callback_answer(call: CallbackQuery, bot: Bot, state: FSMContext):
	await call.answer(cache_time=60)


# Обработка всех колбэков которые потеряли стейты после перезапуска скрипта
@router.callback_query(StateFilter('*'))
async def main_missed_callback(call: CallbackQuery, bot: Bot, state: FSMContext):
	await call.answer('❗️ Кнопка недействительна. Повторите действия заново', True)