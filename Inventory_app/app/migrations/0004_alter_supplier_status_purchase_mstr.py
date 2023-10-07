# Generated by Django 4.2.2 on 2023-09-16 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Purchase_Mstr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('invoice_date', models.DateField(auto_created=True)),
                ('invoice_no', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('status', models.BooleanField(verbose_name=False)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supplier')),
            ],
        ),
    ]