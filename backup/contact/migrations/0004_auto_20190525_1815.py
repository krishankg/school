# Generated by Django 2.2.1 on 2019-05-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190525_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='log',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
