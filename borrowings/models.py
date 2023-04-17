from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models

from books.models import Book
from user.models import User


class Borrowing(models.Model):
    borrow_date = models.DateTimeField(
        validators=[MinValueValidator(limit_value=datetime.now)],
        help_text='The date when the book was borrowed.'
    )
    expected_return_date = models.DateTimeField(
        validators=[MinValueValidator(limit_value=datetime.now)],
        help_text='The date when the book is expected to be returned.'
    )
    actual_return_date = models.DateTimeField(
        validators=[MinValueValidator(limit_value=datetime.now)],
        help_text='The date when the book was actually returned.'
    )
    book = models.ForeignKey(
        Book,
        related_name="borrowings",
        null=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="borrowings",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)


