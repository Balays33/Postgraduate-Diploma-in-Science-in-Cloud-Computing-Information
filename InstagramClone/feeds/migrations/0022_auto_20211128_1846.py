# Generated by Django 2.1 on 2021-11-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0021_auto_20211128_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='uploadTimeF',
            field=models.CharField(default='time', max_length=60),
        ),
    ]