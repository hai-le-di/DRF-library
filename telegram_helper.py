import os

import telebot
import telegram  # this is from python-telegram-bot package
from django.template.loader import render_to_string
from dotenv import load_dotenv

load_dotenv()


# bot = telebot.TeleBot(os.environ["BOT_TOKEN"], parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


# def send_borrowing_notification(borrowing):
#     print("Message Ok")
#     message = f"New borrowing created!\nUser: " \
#               f"{borrowing.user.username}\nBook: {borrowing.book.title}\nBorrow date: {borrowing.borrow_date}\n" \
#               f"Expected return date: {borrowing.expected_return_date}"
#     bot.send_message(chat_id=os.environ["CHAT_ID"], text=message)


def send_borrowing_notification(event):
    print("Message Ok")
    bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
    await bot.send_message(chat_id="@%s" % "Borrowing Notifications",
                           text="hello")
