from django.core.validators import MinValueValidator
from django.db import models
from datetime import date
from books.models import Book
from user.models import User


class Borrowing(models.Model):
    borrow_date = models.DateField(
        validators=[MinValueValidator(limit_value=date.today)],
        help_text='The date when the book was borrowed.'
    )
    expected_return_date = models.DateField(
        validators=[MinValueValidator(limit_value=date.today)],
        help_text='The date when the book is expected to be returned.'
    )
    actual_return_date = models.DateField(
        null=True,
        blank=True,
        help_text='The date when the book was actually returned.'
    )
    book = models.ForeignKey(
        Book,
        related_name="borrowings",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="borrowings",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.book.inventory -= 1
            self.book.save()

        super(Borrowing, self).save(*args, **kwargs)
