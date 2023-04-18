from django.db.models.signals import post_save
from django.dispatch import receiver
from borrowings.models import Borrowing
from telegram_helper import send_borrowing_notification


@receiver(post_save, sender=Borrowing)
def notify_on_new_borrowing(sender, instance, created, **kwargs):
    if created:
        send_borrowing_notification(instance.book, instance.user)
