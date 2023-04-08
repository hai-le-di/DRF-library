from rest_framework import serializers

from books.serializers import BookDetailSerializer
from borrowings.models import Borrowing
from user.serializers import UserSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = "__all__"


class BorrowingListSerializer(BorrowingSerializer):
    book = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="name"
    )
    user = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="title"
    )


class BorrowingDetailSerializer(BorrowingSerializer):
    book = BookDetailSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)
