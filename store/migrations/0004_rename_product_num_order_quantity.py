# Generated by Django 4.1.6 on 2023-09-29 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_product_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product_num',
            new_name='quantity',
        ),
    ]