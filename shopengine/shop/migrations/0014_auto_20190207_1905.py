# Generated by Django 2.1.5 on 2019-02-07 17:05

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20190207_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='head',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True),
        ),
    ]