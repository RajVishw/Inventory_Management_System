# Generated by Django 4.2.2 on 2023-09-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_purchase_mstr_purchase_details_purchase_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_table',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item'),
        ),
        migrations.AlterField(
            model_name='temp_table',
            name='purchase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.purchase_details'),
        ),
        migrations.AlterField(
            model_name='temp_table',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supplier'),
        ),
    ]