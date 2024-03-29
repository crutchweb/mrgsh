# Generated by Django 2.2.3 on 2019-07-23 20:31

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, max_length=200, upload_to='news', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(default=datetime.date(2019, 7, 23), verbose_name='Дата'),
        ),
    ]
