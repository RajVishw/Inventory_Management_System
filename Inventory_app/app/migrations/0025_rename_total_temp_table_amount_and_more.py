# Generated by Django 4.2.2 on 2023-09-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_sale_mstr_sale_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temp_table',
            old_name='total',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='temp_table',
            old_name='product_id',
            new_name='item_id',
        ),
        migrations.RemoveField(
            model_name='sale_mstr',
            name='address',
        ),
        migrations.RemoveField(
            model_name='temp_table',
            name='supplier_id',
        ),
        migrations.AddField(
            model_name='sale_mstr',
            name='totoal',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temp_table',
            name='customer_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temp_table',
            name='number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]