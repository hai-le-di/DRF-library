from rest_framework import viewsets, mixins

from books.permissions import AdminWriteOnly
from borrowings.models import Borrowing
from borrowings.serializers import BorrowingSerializer, BorrowingListSerializer, BorrowingDetailSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    model = Borrowing
    serializer_class = BorrowingSerializer
    permission_classes = (AdminWriteOnly,)
    queryset = Borrowing.objects.select_related("user", "book")

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer

        if self.action == "retrieve":
            return BorrowingDetailSerializer

        return BorrowingSerializer
