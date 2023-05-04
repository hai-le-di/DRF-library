from datetime import date, timedelta, timezone
from unittest import mock

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from books.models import Book
from borrowings.models import Borrowing
from user.models import User


class BorrowingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="user@example.com", password="testpass"
        )
        self.staff_user = User.objects.create_user(
            email="staff@example.com", password="testpass", is_staff=True
        )
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            cover="hard",
            inventory=5,
            daily_fee=1.99,
        )
        self.borrowing = Borrowing.objects.create(
            borrow_date=date.today(),
            expected_return_date=date.today() + timedelta(days=7),
            book=self.book,
            user=self.user,
        )

    def test_borrowing_list(self):
        # Ensure we can retrieve the borrowing list
        self.client.force_authenticate(user=self.user)
        url = reverse("borrowings:borrowings-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrowing_detail(self):
        # Ensure we can retrieve the borrowing detail
        self.client.force_authenticate(user=self.user)
        borrowing = Borrowing.objects.first()
        url = reverse("borrowings:borrowings-detail", args=[borrowing.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @mock.patch("telegram.Bot.send_message")
    def test_create_borrowing(self, mock_send_message):
        self.client.force_authenticate(user=self.user)
        data = {
            "expected_return_date": timezone.now().date(),
            "book": self.book.id,
            "user": self.user.id,
        }
        url = reverse("borrowings:borrowings-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Ensure the borrowing was created successfully
        borrowing = Borrowing.objects.last()
        self.assertEqual(borrowing.book, self.book)
        self.assertEqual(borrowing.user, self.user)
        self.assertEqual(borrowing.expected_return_date, data["expected_return_date"])

    def test_return_borrowing(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("borrowings:return", args=[self.borrowing.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        borrowing = Borrowing.objects.get(id=self.borrowing.id)
        self.assertFalse(borrowing.is_active)
        self.assertIsNotNone(borrowing.actual_return_date)
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.inventory, 6)

    def test_return_already_returned_borrowing(self):
        self.client.force_authenticate(user=self.user)
        self.borrowing.is_active = False
        self.borrowing.actual_return_date = date.today()
        self.borrowing.save()
        url = reverse("borrowings:return", args=[self.borrowing.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_borrowings_as_staff(self):
        self.client.force_authenticate(user=self.staff_user)
        url = reverse("borrowings:borrowings-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
