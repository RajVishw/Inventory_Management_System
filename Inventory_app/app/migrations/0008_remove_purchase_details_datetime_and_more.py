# Generated by Django 4.2.2 on 2023-09-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_purchase_mstr_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_details',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='purchase_mstr',
            name='date',
        ),
        migrations.AlterField(
            model_name='purchase_mstr',
            name='invoice_date',
            field=models.DateField(),
        ),
    ]
