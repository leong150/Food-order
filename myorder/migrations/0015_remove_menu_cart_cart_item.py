# Generated by Django 4.0.6 on 2022-12-13 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myorder', '0014_remove_cart_food_menu_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myorder.menu'),
        ),
    ]
