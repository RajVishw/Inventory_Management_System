# Generated by Django 4.2.2 on 2023-09-19 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_temp_table_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_mstr',
            name='status',
        ),
    ]