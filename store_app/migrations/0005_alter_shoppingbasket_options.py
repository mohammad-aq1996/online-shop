# Generated by Django 4.0.3 on 2022-03-25 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_product_explanation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingbasket',
            options={'ordering': ('buyyer',)},
        ),
    ]
