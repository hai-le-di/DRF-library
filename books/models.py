from django.db import models


class Book(models.Model):
    HARD = "hard"
    SOFT = "soft"
    COVER_CHOICES = (
        (HARD, "hard"),
        (SOFT, "soft"),
    )

    title = models.CharField(max_length=225)
    author = models.CharField(max_length=255)
    cover = models.CharField(choices=COVER_CHOICES, max_length=4),
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=4)

