# Generated by Django 4.2.7 on 2023-11-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='register_token',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
