from django.db import models
from books.models import Book
from user.models import User


class Borrowing(models.Model):
    borrow_date = models.DateField(
        auto_now_add=True, help_text="The date when the book was borrowed."
    )
    expected_return_date = models.DateField(
        help_text="The date when the book is expected to be returned."
    )
    actual_return_date = models.DateField(
        null=True,
        blank=True,
        help_text="The date when the book was actually returned."
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
        if self.actual_return_date and self.is_active is False:
            self.book.inventory += 1
            self.book.save()
        super().save(*args, **kwargs)
