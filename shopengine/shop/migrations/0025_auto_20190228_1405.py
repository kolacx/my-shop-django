# Generated by Django 2.1.5 on 2019-02-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_order_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shop.CartItem'),
        ),
    ]
