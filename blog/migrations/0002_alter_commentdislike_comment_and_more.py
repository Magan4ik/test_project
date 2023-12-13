# Generated by Django 4.2.7 on 2023-11-18 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdislike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.comment'),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
