# Generated by Django 3.0.5 on 2020-04-17 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lazga_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='potato', max_length=150),
        ),
    ]