# Generated by Django 2.1.5 on 2019-03-12 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_mainpage_is_active_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.AlterModelOptions(
            name='mainpage',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
    ]
