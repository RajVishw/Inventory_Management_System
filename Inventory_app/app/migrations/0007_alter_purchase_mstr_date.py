# Generated by Django 4.2.2 on 2023-09-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_purchase_mstr_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_mstr',
            name='date',
            field=models.DateField(auto_created=True),
        ),
    ]