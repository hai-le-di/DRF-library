# Generated by Django 4.2 on 2023-05-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.CharField(
                choices=[("hard", "hard"), ("soft", "soft")],
                default="hard",
                max_length=4,
            ),
            preserve_default=False,
        ),
    ]
