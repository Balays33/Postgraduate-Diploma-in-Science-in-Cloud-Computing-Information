# Generated by Django 2.1.15 on 2021-12-05 13:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0024_feed_locationf'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='createdTimeF',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
