# Generated by Django 4.2.2 on 2023-09-18 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_supplier_status_purchase_mstr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_mstr',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='purchase_mstr',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='Purchase_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item')),
                ('purchase_mstr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.purchase_mstr')),
            ],
        ),
    ]
