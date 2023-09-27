# Generated by Django 4.2.5 on 2023-09-27 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Stores', '0004_alter_store_zip_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('shipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipment_origin', models.CharField(max_length=70)),
                ('expected_date', models.DateField()),
                ('shipment_status', models.CharField(max_length=150)),
                ('shipment_tracking_history', models.CharField(max_length=1000)),
                ('shipment_tracking_link', models.CharField(blank=True, max_length=100, null=True)),
                ('destination_store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.store')),
            ],
        ),
    ]