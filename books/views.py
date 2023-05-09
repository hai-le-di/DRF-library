from rest_framework import viewsets

from books.models import Book
from books.permissions import AdminWriteOnly
from books.serializers import BookSerializer, BookDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AdminWriteOnly,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookDetailSerializer

        return BookSerializer
