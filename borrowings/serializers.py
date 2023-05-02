from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book
from books.serializers import BookDetailSerializer
from borrowings.models import Borrowing
from user.serializers import UserSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = [
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
            "is_active",
        ]

    def validate(self, attrs):
        data = super(BorrowingSerializer, self).validate(attrs)
        Book.validate_book(attrs["book"], ValidationError)

        return data

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        book.save()
        borrowing = Borrowing.objects.create(
            book=book,
            user=self.context["request"].user,
            borrow_date=timezone.now(),
            expected_return_date=validated_data["expected_return_date"],
        )
        return borrowing


class BorrowingListSerializer(BorrowingSerializer):
    book = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="title"
    )
    user = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="email"
    )


class BorrowingDetailSerializer(BorrowingSerializer):
    book = BookDetailSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)
