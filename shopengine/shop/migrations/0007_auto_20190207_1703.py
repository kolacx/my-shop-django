# Generated by Django 2.1.5 on 2019-02-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190207_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Заголовок', max_length=200, verbose_name='Заголовок'),
        ),
    ]
