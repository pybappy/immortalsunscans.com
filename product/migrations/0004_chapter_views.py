# Generated by Django 3.0.7 on 2020-12-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
