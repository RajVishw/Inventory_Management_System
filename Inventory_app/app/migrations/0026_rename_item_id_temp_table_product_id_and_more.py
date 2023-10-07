# Generated by Django 4.2.2 on 2023-09-21 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_total_temp_table_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temp_table',
            old_name='item_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='temp_table',
            old_name='amount',
            new_name='total',
        ),
        migrations.RemoveField(
            model_name='temp_table',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='temp_table',
            name='number',
        ),
        migrations.AddField(
            model_name='temp_table',
            name='supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.supplier'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Temp_Table_Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('invoice_no', models.CharField(max_length=50)),
                ('invoice_date', models.DateField()),
                ('number', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item')),
            ],
        ),
    ]