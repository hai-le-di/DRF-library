import os
from borrowings.celery import app
from datetime import timedelta
from django.utils import timezone
from .models import Borrowing
from telegram_helper import bot
from dotenv import load_dotenv

load_dotenv()


@app.task
def send_overdue_notifications():
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)

    overdue_borrowings = Borrowing.objects.filter(
        expected_return_date__lte=tomorrow,
        actual_return_date__isnull=True,
        is_active=True,
    )

    chat_id = os.environ["CHAT_ID"]

    # Send a notification for each overdue borrowing
    for borrowing in overdue_borrowings:
        book_title = borrowing.book.title
        user_email = borrowing.user.email
        borrow_date = borrowing.borrow_date.strftime("%Y-%m-%d")
        expected_return_date = borrowing.expected_return_date.strftime("%Y-%m-%d")

        # Compose the message for the notification
        message = (
            f'The book "{book_title}" borrowed by {user_email} '
            f"on {borrow_date} is overdue. Expected return date is "
            f"{expected_return_date}."
        )

        # Send the notification
        bot.send_message(chat_id=chat_id, text=message)
