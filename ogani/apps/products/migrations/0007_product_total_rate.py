# Generated by Django 3.2.13 on 2022-06-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productimage_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_rate',
            field=models.FloatField(default=0),
        ),
    ]
