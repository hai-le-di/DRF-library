from django.db import models
from rest_framework.exceptions import ValidationError


class Book(models.Model):
    HARD = "hard"
    SOFT = "soft"
    COVER_CHOICES = (
        (HARD, "hard"),
        (SOFT, "soft"),
    )

    title = models.CharField(max_length=225)
    author = models.CharField(max_length=255)
    cover = models.CharField(choices=COVER_CHOICES, max_length=4)
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=4)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(inventory__gte=0),
                name='inventory_non_negative'
            ),
        ]

    def __str__(self):
        return self.title

    @staticmethod
    def validate_book(book, error_to_raise):
        if book.inventory < 0:
            raise error_to_raise("Book is out of stock")

    def clean(self):
        Book.validate_book(self, ValidationError)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()
        return super(Book, self).save(
            force_insert,
            force_update,
            using,
            update_fields
        )
