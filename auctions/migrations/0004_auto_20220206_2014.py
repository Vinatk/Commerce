# Generated by Django 3.2.6 on 2022-02-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20220206_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='createlisting',
            name='watchers',
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='createlisting',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.Comment'),
        ),
    ]
