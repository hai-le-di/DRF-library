import os

from telegram import Bot

bot = Bot(token=os.environ["BOT_TOKEN"])


def send_borrowing_notification(book, user):
    message = f"New borrowing created!\nUser: " \
              f"{user.username}\nBook: {book.title}\nBorrow date: {book.borrow_date}\n" \
              f"Expected return date: {book.expected_return_date}"
    bot.send_message(chat_id=os.environ["CHAT_ID"], text=message)
