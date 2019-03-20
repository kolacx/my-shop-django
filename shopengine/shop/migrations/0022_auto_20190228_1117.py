# Generated by Django 2.1.5 on 2019-02-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_menu_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('status', models.CharField(choices=[('Создан', 'Создан'), ('ONECLICK', 'One Click'), ('Подтвержденный', 'Подтвержденный'), ('В Обработке', 'В обработке'), ('Отменен', 'Отменен'), ('Отправлен', 'Отправлен')], default='Создан', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='cart_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='item_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shop.Card'),
        ),
    ]