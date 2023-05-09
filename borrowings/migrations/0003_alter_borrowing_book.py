# Generated by Django 4.2 on 2023-05-01 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
        ("borrowings", "0002_borrowing_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="borrowings",
                to="books.book",
            ),
        ),
    ]
