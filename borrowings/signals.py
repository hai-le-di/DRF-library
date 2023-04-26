from django.db.models.signals import post_save
from django.dispatch import receiver

from borrowings.models import Borrowing
from telegram_helper import send_borrowing_notification


@receiver(post_save, sender=Borrowing)
def notify_on_borrowing_creation(sender, instance, created, **kwargs):
    """
    Sends a notification when a new borrowing is created.
    """
    if created:
        print("Borrowing OK")
        send_borrowing_notification(instance)
