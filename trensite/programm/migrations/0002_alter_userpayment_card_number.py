# Generated by Django 4.2.6 on 2023-11-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpayment',
            name='card_number',
            field=models.CharField(error_messages='Неправильная карта', max_length=16, verbose_name='Номер карты'),
        ),
    ]
