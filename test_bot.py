import os
from datetime import date, timedelta
from unittest import TestCase, mock
from telebot import TeleBot

from books.models import Book
from telegram_helper import send_borrowing_notification
from borrowings.models import Borrowing
from user.models import User


class TestTelegramHelper(TestCase):
    def setUp(self):
        self.bot_token = "test_token"
        self.chat_id = "test_chat_id"
        os.environ["BOT_TOKEN"] = self.bot_token
        os.environ["CHAT_ID"] = self.chat_id

    @mock.patch.object(TeleBot, "send_message")
    def test_send_borrowing_notification(self, mock_send_message):
        user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass'
        )
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            cover='hard', inventory=5,
            daily_fee=1.99
        )
        borrowing = Borrowing.objects.create(borrow_date=date.today(),
                                             expected_return_date=date.today() + timedelta(days=7),
                                             book=book,
                                             user=user,
                                             )
        with mock.patch('telegram_helper.bot'):
            send_borrowing_notification(borrowing.id)
            mock_send_message.assert_called_once_with(
                chat_id=self.chat_id,
                text=f"New borrowing created!\nUser email: {borrowing.user.email}\n"
                     f"Book: {borrowing.book.title}\nBorrow date: {borrowing.borrow_date}\n"
                     f"Expected return date: {borrowing.expected_return_date}",
            )
