# Generated by Django 3.1.2 on 2020-11-14 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20201114_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='totalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]