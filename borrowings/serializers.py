from django.utils import timezone
from rest_framework import serializers

from books.models import Book
from books.serializers import BookDetailSerializer
from borrowings.models import Borrowing
from user.serializers import UserSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['borrow_date'] = instance.borrow_date.strftime('%Y-%m-%d %H:%M:%S')
        representation['expected_return_date'] = instance.expected_return_date.strftime('%Y-%m-%d %H:%M:%S')
        representation['actual_return_date'] = instance.expected_return_date.strftime('%Y-%m-%d %H:%M:%S')
        return representation

    def validate(self, attrs):
        data = super(BorrowingSerializer, self).validate(attrs)
        Book.validate_book(attrs["book"], serializers.ValidationError)

        return data

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        book.save()
        borrowing = Borrowing.objects.create(
            book=book,
            user=self.request.user,
            borrow_date=timezone.now(),
            expected_return_date=validated_data["expected_return_date"]
        )
        return borrowing


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
