# Generated by Django 3.1.2 on 2020-11-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='productimage',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
