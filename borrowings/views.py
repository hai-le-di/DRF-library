from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from books.permissions import AdminWriteOnly
from borrowings.models import Borrowing
from borrowings.serializers import BorrowingSerializer, BorrowingListSerializer, BorrowingDetailSerializer


class BorrowingViewSet(viewsets.ModelViewSet):
    model = Borrowing
    serializer_class = BorrowingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Borrowing.objects.select_related("book", "user")

    def get_queryset(self):
        if self.request.query_params.get('is_active'):
            return Borrowing.objects.filter(user=self.request.user, is_active=True)
        else:
            return Borrowing.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer

        if self.action == "retrieve":
            return BorrowingDetailSerializer

        return BorrowingSerializer
