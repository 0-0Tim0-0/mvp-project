# Generated by Django 5.1.2 on 2024-10-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='view',
        ),
        migrations.AddField(
            model_name='rent',
            name='vie',
            field=models.CharField(default=2, max_length=30, verbose_name='Просмотры'),
            preserve_default=False,
        ),
    ]
