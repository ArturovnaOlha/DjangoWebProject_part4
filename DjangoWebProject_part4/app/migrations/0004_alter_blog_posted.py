# Generated by Django 4.2.16 on 2024-10-27 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blog_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 27, 15, 27, 1, 760613), verbose_name='Опубликована'),
        ),
    ]
