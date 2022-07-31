# Generated by Django 4.0.6 on 2022-07-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookNo', models.IntegerField(verbose_name='Book Number')),
                ('BookName', models.CharField(max_length=200, verbose_name='Book Name')),
                ('AuthorName', models.CharField(max_length=200, verbose_name='Author Name')),
                ('RegId', models.CharField(max_length=50, verbose_name='Register Id')),
                ('IssuedDate', models.DateField(auto_now_add=True, verbose_name='Issued Date')),
                ('IsReturned', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=50, verbose_name='IS RETURNED')),
            ],
        ),
    ]