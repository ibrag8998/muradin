# Generated by Django 3.2.4 on 2021-06-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.PositiveSmallIntegerField(choices=[(1, 'телефон'), (2, 'почта')], default=1, verbose_name='Тип контакта')),
                ('contact', models.CharField(max_length=255, verbose_name='Контакт')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='clients.client')),
            ],
            options={
                'verbose_name': 'контакт клиента',
                'verbose_name_plural': 'контакты клиента',
            },
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='clients.client')),
            ],
            options={
                'verbose_name': 'адрес клиента',
                'verbose_name_plural': 'адреса клиента',
            },
        ),
    ]
