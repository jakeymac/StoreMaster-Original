# Generated by Django 4.2.5 on 2023-09-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
