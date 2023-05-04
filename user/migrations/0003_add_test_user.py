from django.db import migrations
from user.models import User


def create_test_user(apps, schema_editor):
    test_user = User.objects.create_user(
        email="test@user.test",
        password="testpassword"
    )


def reverse_func(apps, schema_editor):
    User = apps.get_model("user", "User")
    User.objects.filter(email="test@user.test").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_managers_remove_user_username_and_more'),
    ]

    operations = [
        migrations.RunPython(create_test_user, reverse_func),
    ]
