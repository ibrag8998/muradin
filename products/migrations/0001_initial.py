# Generated by Django 3.2.4 on 2021-06-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество товара на складе')),
                ('category', models.CharField(blank=True, max_length=255, verbose_name='Категория товара')),
                ('arrival_date', models.DateField(verbose_name='Дата прибытия')),
                ('cost_price', models.PositiveIntegerField(verbose_name='Себестоимость')),
                ('retail_price', models.PositiveIntegerField(verbose_name='Розничная цена')),
            ],
            options={
                'verbose_name': 'товар на складе',
                'verbose_name_plural': 'товары на складе',
            },
        ),
    ]
