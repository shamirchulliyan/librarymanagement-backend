# Generated by Django 4.0.6 on 2022-08-05 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LIB', '0006_alter_book_dateofentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='Book',
        ),
    ]
