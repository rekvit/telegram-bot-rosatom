from aiogram.dispatcher import FSMContext

from DatabaseModels.Worker import Worker
from DatabaseModels.admin import Admin
from app import bot, dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from aiogram.utils.exceptions import BotBlocked

from main.config import admin_id, States, ROSATOM_SITE, Authorized_states
from main.helpers.menu import main_menu, back_to_menu, hide_menu, generate_workers_buttons
from main.helpers.smiles import create_smile


async def on_start_message(dispatcher):
    """
    При запуске скрипта бота
    :param dispatcher:
    :return:
    """
    await bot.send_message(chat_id=admin_id, text="Бот запущен!",
                           reply_markup=main_menu())


async def on_finish_message(dispatcher):
    print("Бот остановлен!")


@dispatcher.message_handler(Command("start"), state="*")
async def start_conversation(message: Message):
    """
    При первом запуске бота
    :param message:
    :return:
    """
    if Worker.check_worker_exists(message.from_user):
        await States.COMMAND_STATE.set()
        await general_menu(message)
    else:
        await States.ENTER_EMAIL_STATE.set()
        await message.answer(text="Давайте пройдем простую процедуру регистрации. Это займет не более двух минут")
        await message.answer(text="Введите ваш E-mail:", reply_markup=hide_menu())
        # await bot.send_message(chat_id=admin_id, text=f"Новая заявка на регистрацию: @{message.from_user.username}")
        # await message.answer(text="Запрос на вашу регистрацию направлен администратору", reply_markup=hide_menu())


@dispatcher.message_handler(Command("menu"), state=Authorized_states)
@dispatcher.message_handler(Text("В меню"), state=Authorized_states)
async def general_menu(message: Message): # , state: FSMContext
    """
    Команда показать меню
    :param message:
    :return:
    """
    # async with state.proxy() as userdata:
    #     userdata.clear()
    await message.answer(text="Выбери действие", reply_markup=main_menu(message.from_user))
    await States.COMMAND_STATE.set()


@dispatcher.message_handler(Text("Сайт компании" + create_smile("\\ud83c\\udf10")), state=Authorized_states)
async def go_to_web_site(message: Message):
    await message.answer(text=f"<a href=\"{ROSATOM_SITE}\">{ROSATOM_SITE}</a>", parse_mode="HTML")


@dispatcher.errors_handler()
async def on_error(update, error):
    print(error)
    return True
