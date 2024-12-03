# Generated by Django 5.1.2 on 2024-12-03 15:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_product'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.products')),
            ],
            options={
                'unique_together': {('cart', 'product')},
            },
        ),
    ]
