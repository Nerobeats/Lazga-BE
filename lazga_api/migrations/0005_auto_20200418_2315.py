# Generated by Django 3.0.5 on 2020-04-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lazga_api', '0004_auto_20200418_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='selling_counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
