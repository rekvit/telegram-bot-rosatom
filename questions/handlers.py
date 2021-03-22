from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from main.config import admin_id, States
from app import bot, dispatcher
from main.handlers import general_menu
from main.helpers.menu import hide_menu, question_menu, back_to_menu
from main.helpers.smiles import create_smile
from DatabaseModels.Worker import Worker


@dispatcher.message_handler(Text("Другие вопросы" + create_smile("\\u2753")), state="*")
async def other_questions(message: Message):
    """
    Меню "Другие вопросы" (название может меняться)
    :param message:
    :return:
    """
    await message.answer(text="Другие вопросы:\n", reply_markup=question_menu())


# Другие вопросы -> Типичные вопросы. Типичные вопросы можно прям тут описать - это нормальная практика.
# Штук 6-8 будет достаточно
@dispatcher.message_handler(Text("Типичные вопросы" + create_smile("\\u2754")), state="*")
async def typical_questions(message: Message):
    """
    Команда типичные вопросы
    To Do: сделать считывание типичных вопросов из файла
    :param message:
    :return:
    """
    await message.answer(text="Типичные вопросы: \nГде находится Мадагаскар? - На острове Мадагаскар!" +
                              "\n",
                         reply_markup=back_to_menu())


# Другие вопросы -> Задать вопрос.
@dispatcher.message_handler(Text("Задать вопрос" + create_smile("\\ud83d\\udcdd")), state="*")
async def ask_new_question(message: Message):
    """
    Команда задать новый вопрос
    :param message:
    :return:
    """
    await States.ENTER_TEXT_STATE.set()
    await message.answer(text="Задать вопрос\n\nНапишите Ваш вопрос:\n\n\n",
                         reply_markup=back_to_menu())
# hmm


@dispatcher.message_handler(state=States.ENTER_TEXT_STATE)
async def resend_message_to_boss(message: Message):
    """
    Перенаправляет сообщение начальнику (админу)
    :param message:
    :return:
    """
    await States.COMMAND_STATE.set()
    text = f"@{message.chat.username} задает вопрос: {message.text}"
    await bot.send_message(chat_id=admin_id, text=text)
    await message.answer(text="Ваш вопрос успешно задан.\nОтвет придёт вам в личные сообщения от администратора.\n")
    await general_menu(message)


@dispatcher.message_handler(Text("Моя должность" + create_smile("\\ud83d\\udcbc")), state="*")
async def my_post(message: Message):
    """
    Выводит текущий статус сотрудника, его должность и ЗП
    :param message:
    :return:
    """
    connection = Worker()
    worker = connection.get_worker(message.from_user)
    text_html = f'<b>ФИО: </b><i>{worker["Firstname"]} {worker["Lastname"]}</i>\n' \
                f'<b>Должность: </b><i>{worker["Title"]}</i>\n' \
                f'<b>Зарплата: </b><i>{worker["Salary"]}</i>\n'
    await message.answer(text=text_html, parse_mode="HTML")
    # await message.answer(text=f'Должность: {worker["Title"]}', parse_mode="HTML")
    # await message.answer(text=f'Зарплата: {worker["Salary"]}', parse_mode="HTML")

