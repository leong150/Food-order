# Generated by Django 4.0.6 on 2023-02-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myorder', '0019_remove_cart_item_menu_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
