from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from books.models import Book
from books.permissions import AdminWriteOnly
from books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AdminWriteOnly, )
