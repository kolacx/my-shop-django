# Generated by Django 2.1.5 on 2019-02-07 13:58

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=shop.models.image_folder),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='properties',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Свойства'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Характеристики'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок'),
        ),
    ]
