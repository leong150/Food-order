# Generated by Django 4.0.6 on 2023-01-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myorder', '0017_remove_cart_qty_cart_order_no_menu_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
