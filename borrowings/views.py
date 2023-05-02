from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from borrowings.models import Borrowing
from borrowings.serializers import (
    BorrowingSerializer,
    BorrowingListSerializer,
    BorrowingDetailSerializer,
)


class BorrowingViewSet(viewsets.ModelViewSet):
    model = Borrowing
    serializer_class = BorrowingSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Borrowing.objects.select_related("book", "user")

    def get_queryset(self):
        user = self.request.user
        user_id = self.request.query_params.get("user_id", None)

        if user.is_staff and user_id:
            return Borrowing.objects.filter(user_id=user_id)
        elif user.is_staff:
            return Borrowing.objects.all()
        else:
            return Borrowing.objects.filter(user=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer

        if self.action == "retrieve":
            return BorrowingDetailSerializer

        return BorrowingSerializer

    @action(detail=True, methods=["post"])
    def return_borrowing(self, request, pk=None):
        borrowing = self.get_object()
        if not borrowing.is_active:
            return Response(
                {"message": "Borrowing has already been returned."}, status=400
            )
        borrowing.is_active = False
        borrowing.actual_return_date = timezone.now().date()
        borrowing.book.inventory += 1
        borrowing.book.save(update_fields=["inventory"])
        borrowing.save(update_fields=["is_active", "actual_return_date"])
        serializer = self.get_serializer(borrowing)
        return Response(serializer.data)
