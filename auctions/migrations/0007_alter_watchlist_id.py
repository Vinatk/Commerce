# Generated by Django 3.2.6 on 2022-02-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20220206_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]