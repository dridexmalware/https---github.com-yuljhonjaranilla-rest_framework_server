# Generated by Django 5.0.4 on 2024-04-21 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=255, unique=True),
        ),
    ]
