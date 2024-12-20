# Generated by Django 4.2.16 on 2024-10-29 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_comment_options_alter_blog_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 29, 13, 49, 38, 729956), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 29, 13, 49, 38, 730956), verbose_name='Дата комментария'),
        ),
    ]
