# Generated by Django 2.1.5 on 2019-03-12 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20190312_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ooo', to='shop.Order'),
        ),
    ]
