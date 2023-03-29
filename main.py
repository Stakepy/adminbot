import telebot

# Сюда пишем токен созданный BotFather
token = ''
# Создаем экземпляр бота
bot = telebot.TeleBot(token)
# Получаем айди чата по его имени
GROUP_ID = 0000000000000
# Список запрещённых слов которые нужно удалять
blacklist = ['']

# Перехват чужих сообщений в чате
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # По очереди ищем запрещённые слова из списка в сообщении
    for x in blacklist:
        if (x in message.text):
            # Если найдены запрещённые слова удаляем сообщение с ними
            bot.delete_message(message.chat.id, message.message_id)
        else:
            pass


if __name__ == "__main__":
    bot.infinity_polling()
