# Generated by Django 5.0.3 on 2024-07-29 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='purchased_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 17, 35, 44, 74318, tzinfo=datetime.timezone.utc)),
        ),
    ]
