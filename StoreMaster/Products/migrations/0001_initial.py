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
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product_price', models.FloatField()),
                ('product_location', models.CharField(max_length=10)),
                ('product_stock', models.IntegerField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stores.store')),
            ],
        ),
    ]