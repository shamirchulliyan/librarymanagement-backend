# Generated by Django 4.0.6 on 2022-08-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIB', '0005_alter_book_authorname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='DateofEntry',
            field=models.DateField(blank=True, null=True, verbose_name='DATE OF ENTRY'),
        ),
    ]
