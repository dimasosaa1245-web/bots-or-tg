import telebot
import re

TOKEN = "8707896192:AAEbOeRfokfVzXY1FQgOkoD4_04pDRA1hyY"

bot = telebot.TeleBot(TOKEN)

@bot.channel_post_handler(func=lambda m: True)
def handle_channel_post(message):
    text = message.text or ""

    print(f"Сообщение: {text}")

    match = re.search(r"від\s+(.+?)\s+до\s+(.+)", text, re.IGNORECASE)

    if match:
        start = match.group(1).strip()
        end = match.group(2).strip()

        data = {
            "type": "shahed",
            "from": start,
            "to": end
        }

        print(data)

bot.infinity_polling(skip_pending=True)