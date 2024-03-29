# Generated by Django 4.0.6 on 2023-02-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myorder', '0021_alter_cart_order_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.PositiveIntegerField(blank=True)),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='order_no',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='sum',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='qty',
        ),
        migrations.AddField(
            model_name='cart',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myorder.menu'),
        ),
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myorder.order'),
        ),
    ]
