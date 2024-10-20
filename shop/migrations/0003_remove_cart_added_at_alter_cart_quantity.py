# Generated by Django 5.0.7 on 2024-10-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='added_at',
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
