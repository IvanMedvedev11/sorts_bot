from dotenv import load_dotenv
from time import perf_counter
from math import fsum
from functions import *
import os
import telebot
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который сортирует списки чисел. Чтобы отсортировать список, просто введите числа(или отправьте .txt файл с ними) через запятую: ")
@bot.message_handler(content_types=['text'])
def sort(message):
    numbers = message.text.split(", ")
    try:
        numbers = list(map(float, numbers))
    except ValueError:
        bot.send_message(message.chat.id, "Извините, но вы ввели не совсем верный список чисел(есть лишний символ), попробуйте еще раз")
    else:
        tic = perf_counter()
        if fsum(numbers) / len(numbers) <= 1.0:
            numbers = bubble_sort(numbers)
        elif fsum(numbers) / len(numbers) <= 1000.0:
            numbers = merge_sort(numbers)
        else:
            numbers = sorted(numbers)
        toc = perf_counter()
        bot.send_message(message.chat.id, f"Отсортированный список: {numbers}. \nПотраченное время: {toc - tic}")
@bot.message_handler(content_types=['document'])
def handle_document(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    if message.document.mime_type == 'text/plain':
        with open('file.txt', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, 'Файл успешно получен и сохранен!')
        with open('file.txt', 'r') as new_file:
            numbers = new_file.read()
            numbers = numbers.split(', ')
            print(numbers)
        try:
            numbers = list(map(float, numbers))
        except ValueError:
            bot.send_message(message.chat.id,"Извините, но вы отправили не совсем верный список чисел(есть лишний символ), попробуйте еще раз")
        else:
            tic = perf_counter()
            if fsum(numbers) / len(numbers) <= 1.0:
                numbers = bubble_sort(numbers)
            elif fsum(numbers) / len(numbers) <= 1000.0:
                numbers = merge_sort(numbers)
            else:
                numbers = sorted(numbers)
            toc = perf_counter()
            bot.send_message(message.chat.id, f"Отсортированный список: {numbers}. \nПотраченное время: {toc - tic}")
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте файл в формате .txt.')
bot.infinity_polling()
