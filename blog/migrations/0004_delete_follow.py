# Generated by Django 4.2.7 on 2023-11-18 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]