# Generated by Django 3.1.2 on 2020-11-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_auto_20201117_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='totalprice',
        ),
    ]
