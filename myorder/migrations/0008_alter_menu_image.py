# Generated by Django 4.0.6 on 2022-11-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myorder', '0007_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]