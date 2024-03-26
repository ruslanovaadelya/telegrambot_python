# import telebot
# from telebot import types
# from config import TOKEN

# bot  = telebot.TeleBot(TOKEN)

# menu = types.ReplyKeyboardMarkup(resize_keyboard= True)
# menu.row("Супы" , "Горячие блюда")
# menu.row("Десерты","Напитки")



# dish = types.ReplyKeyboardMarkup(resize_keyboard= True)
# dish.row("Блюдо 1","Блюдо 2","Блюдо 3")
# dish.row("Вернутся в меню")


# @bot.message_handler(commands=['start'])

# def start(message):
#     bot.send_message(message.chat.id,"Добро пожаловать в наш ресторан, для вас доступно электронное меню",reply_markup=menu)

# @bot.message_handler(func=lambda message:True)

# def second(message):
#     if message.text == "Супы":
#         bot.send_message(message.chat.id, "Выберите суп",reply_markup=dish)
#     elif message.text == "Горячие блюда":
#         bot.send_message(message.chat.id, "Выберите блюдо",reply_markup=dish)
#     elif message.text == "Десерты":
#         bot.send_message(message.chat.id, "Выберите десерт",reply_markup=dish)
#     elif message.text == "Напитки":
#         bot.send_message(message.chat.id, "Выберите напиток",reply_markup=dish)
#     elif message.text == "Вернутся в меню":
#         bot.send_message(message.chat.id, "Идем в меню",reply_markup=menu)
#     elif message.text in ["Блюдо 1","Блюдо 2","Блюдо 3"]:
#         bot.send_message(message.chat.id,f"вы выбрали {message.text}")


# bot.polling(non_stop=True)
#------------------------------------------
# create user delia with password '1';
# CREATE ROLE
# postgres=# create database good with owner delia;
# CREATE DATABASE
# postgres=# grant all privileges on database good to delia;
# GRANT
# postgres=# \c good
# You are now connected to database "good" as user "postgres".
# good=# 
#=============================================================

import psycopg2
import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Наша группа","О нас")


user = types.ReplyKeyboardMarkup(resize_keyboard=True)
user.row("Ментор","Ассистенты","Студенты")
user.row("Вернутся назад")

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id,"Приветствую в ITCbootcamp,выберите что хотите узнать.",reply_markup=menu)

@bot.message_handler(func=lambda message:True)
def second(message):
    if message.text == "Наша группа":
        bot.send_message(message.chat.id, "Кто вас интересует",reply_markup=user)
    elif message.text == "Ментор":
            bot.send_message(message.chat.id,"Нашего ментора зовут Аркадий ему 29 и он крутой",reply_markup=user)
    elif message.text == "Ассистенты":
            bot.send_message(message.chat.id,"У нас 3 ассистента. Их зовут Антон,Элиза,ДиКаприо",reply_markup=user)
    elif message.text == "Студенты":
            bot.send_message(message.chat.id,"В нашей группе 5 студентов.Бир байке,Макс ,Тимур,Владислав,Аделя.",reply_markup=user)
    elif message.text == "Вернутся в назад":
            bot.send_message(message.chat.id, "Вернемся назад",reply_markup=menu)
    elif message.text == "О нас":
        bot.send_message(message.chat.id, "Наш адрес :Раззакова 32, инстаграм:www.instagram.com/itc_bootcamp?igsh=ajk1b2phbXU4b213",reply_markup=menu)
    elif message.text in ["Ментор","Ассистенты","Студенты"]:
        bot.send_message(message.chat.id,f"вы выбрали {message.text}")


bot.polling(non_stop=True)


