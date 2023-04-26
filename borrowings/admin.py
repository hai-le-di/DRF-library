from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Borrowing


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'borrow_date', 'expected_return_date', 'actual_return_date', 'is_active']


admin.site.unregister(Group)
