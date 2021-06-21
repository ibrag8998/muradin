# Generated by Django 3.2.4 on 2021-06-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
        ('products', '0002_alter_product_cost_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='providers.provider', verbose_name='Поставщик'),
            preserve_default=False,
        ),
    ]