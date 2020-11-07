# Generated by Django 3.1.2 on 2020-11-06 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0006_auto_20201106_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='address',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
