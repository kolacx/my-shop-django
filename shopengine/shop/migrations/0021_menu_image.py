# Generated by Django 2.1.5 on 2019-02-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20190222_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
