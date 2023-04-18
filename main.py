import sqlite3

import telebot

from config import TOKEN
from config_buttons.keyboards import *
from telebot.types import Message, CallbackQuery
from auth import *

# ПОДКЛЮЧЕНИЕ БОТА
bot = telebot.TeleBot(TOKEN)

name = ''
phone_number = 0
connect = sqlite3.connect('database/users.db')
cursor = connect.cursor()


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    if message.from_user.username in AUTH:
        msg = bot.send_message(chat_id=message.chat.id,
                               text=welcome_text['is_valid_sign'],
                               reply_markup=markup_general)

    else:
        reg = bot.send_message(chat_id=message.chat.id,
                               text=welcome_text['is_error_sign'],
                               reply_markup=markup_register)


# REGISTER

@bot.callback_query_handler(func=lambda call: call.data == 'register')
def register(call: CallbackQuery):
    if call.data == 'register':
        bot.send_message(call.message.chat.id, text='Здраствуйте! Как вас зовут?')
        bot.register_next_step_handler(call.message, reg_name)


@bot.callback_query_handler(func=lambda call: call.data == 'sign_out')
def register(call: CallbackQuery):
    if call.data == 'sign_out':
        bot.delete_message(call.message.chat.id, call.message.message_id)


# REGISTRATION BLOCK


@bot.message_handler(commands=['registration'])
def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Ваш номер телефона WhatsApp:')
    bot.register_next_step_handler(message, reg_number)


def reg_number(message):
    global phone_number
    phone_number = message.text
    check_is_validate = '*Перепроверьте вашу информацию!*\n' + '--------------------------------------\n' + 'Ваше имя : ' + name + '\n' + 'Номер телефона : ' + phone_number + '\n' + 'Ваш username : ' + message.from_user.username + '\n' + '--------------------------------------\n' + '*Все правильно?*'
    bot.send_message(message.from_user.id, check_is_validate, parse_mode="Markdown", reply_markup=agree_or_not_agree)


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def register(call: CallbackQuery):
    new_request_from_user = 'Имя: ' + name + '\n' + 'Номер телефона: ' + str(
        phone_number) + '\n' + 'UserName: ' + call.message.chat.username

    if call.data == 'yes':
        channel_id = -1001985776273  # Здесь укажите ID Вашего канала
        check = bot.send_message(channel_id, str(new_request_from_user), reply_markup=markup_reguest_from_user)
        bot.send_message(call.message.chat.id,
                         'Ваша заявка на рассмотрении! Если администратор посчитает нужным вас добавить, то вы будете участником нашей группы)')
        bot.delete_message(call.message.chat.id, check.message_id)

        # users.append(call.from_user.username)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, text='Здраствуйте! Как вас зовут?')
        bot.register_next_step_handler(call.message, reg_name)


# ADD OR DELETE IN ADMIN CHANEL


@bot.callback_query_handler(func=lambda call: call.data == 'add_user')
def adding_or_delete(call: CallbackQuery):
    if call.data == 'add_user':
        bot.send_message(call.message.chat.id, text=f'{call.from_user.username} успешно добавлен!')
        bot.delete_message(call.message.chat.id, call.message.chat.id)


# AFTER SIGNIN


if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=123)
