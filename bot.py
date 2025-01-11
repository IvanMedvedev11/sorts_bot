import telebot
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который сортирует списки чисел. Чтобы отсортировать список, просто введите числа через запятую: ")
@bot.message_handler(content_types=['text'])
def sort(message):
    numbers = message.text.split(", ")
    print(numbers)
    numbers = list(map(float, numbers))
    numbers = bubble_sort(numbers)
    bot.send_message(message.chat.id, f"Отсортированный список: {numbers}")
bot.infinity_polling()
