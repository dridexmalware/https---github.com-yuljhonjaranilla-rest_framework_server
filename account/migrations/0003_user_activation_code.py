# Generated by Django 5.0.4 on 2024-04-21 06:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]