import os
import telebot
from dotenv import load_dotenv
from borrowings.models import Borrowing

load_dotenv()


bot = telebot.TeleBot(os.environ["BOT_TOKEN"])


def send_borrowing_notification(borrowing_id):
    borrowing = Borrowing.objects.get(id=borrowing_id)
    message = f"New borrowing created!\nUser email: " \
              f"{borrowing.user.email}\nBook: {borrowing.book.title}\nBorrow date: {borrowing.borrow_date}\n" \
              f"Expected return date: {borrowing.expected_return_date}"
    bot.send_message(chat_id=os.environ["CHAT_ID"], text=message)
