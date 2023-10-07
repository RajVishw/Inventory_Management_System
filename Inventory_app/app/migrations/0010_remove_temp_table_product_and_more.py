# Generated by Django 4.2.2 on 2023-09-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_temp_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temp_table',
            name='product',
        ),
        migrations.RemoveField(
            model_name='temp_table',
            name='supplier_name',
        ),
        migrations.AddField(
            model_name='temp_table',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='temp_table',
            name='supplier_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='temp_table',
            name='purchase_id',
            field=models.IntegerField(default=0),
        ),
    ]