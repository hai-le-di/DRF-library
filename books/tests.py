from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from books.models import Book
from books.serializers import BookSerializer
from user.models import User


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            email='admin@test.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.admin_user)

    def test_create_book(self):
        url = reverse('books:book-list')
        data = {
            'title': 'The Catcher in the Rye',
            'author': 'J.D. Salinger',
            'cover': 'hard',
            'inventory': 10,
            'daily_fee': 2.99,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'The Catcher in the Rye')

    def test_list_books(self):
        Book.objects.create(
            title='The Catcher in the Rye',
            author='J.D. Salinger',
            cover='hard',
            inventory=10,
            daily_fee=2.99,
        )
        url = reverse('books:book-list')
        response = self.client.get(url, format='json')
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_book(self):
        book = Book.objects.create(
            title='The Catcher in the Rye',
            author='J.D. Salinger',
            cover='hard',
            inventory=10,
            daily_fee=2.99,
        )
        url = reverse('books:book-detail', args=[book.id])
        response = self.client.get(url)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        book = Book.objects.create(
            title='The Catcher in the Rye',
            author='J.D. Salinger',
            cover='hard',
            inventory=10,
            daily_fee=2.99,
        )
        url = reverse('books:book-detail', args=[book.id])
        data = {'title': 'The Catcher in the Rye (Updated)'}
        response = self.client.patch(url, data, format='json')
        book.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.title, 'The Catcher in the Rye (Updated)')

    def test_delete_book(self):
        book = Book.objects.create(
            title='The Catcher in the Rye',
            author='J.D. Salinger',
            cover='hard',
            inventory=10,
            daily_fee=2.99,
        )
        url = reverse('books:book-detail', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
