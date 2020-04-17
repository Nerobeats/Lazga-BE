# Generated by Django 3.0.5 on 2020-04-17 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image_url', models.URLField(default='https://pbs.twimg.com/profile_images/1046609638425268224/-pJ9ZOS9_400x400.jpg')),
                ('description', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(max_length=200)),
                ('itemPrice', models.DecimalField(decimal_places=2, default=17.0, max_digits=5)),
                ('added_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('PR', 'preparing order'), ('OD', 'out for delivery'), ('DV', 'delivered'), ('PS', 'canceled'), ('NS', 'not submitted')], default='NS', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('RT', 'tshirt'), ('HD', 'hoodie'), ('MG', 'mug'), ('PS', 'popsocket'), ('PR', 'poster'), ('ST', 'sticker'), ('CR', 'coaster'), ('LS', 'long sleeve')], default='RT', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='0', max_length=50)),
                ('size', models.CharField(default='0', max_length=50)),
                ('magic', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lazga_api.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lazga_api.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='lazga_api.OrderItem', to='lazga_api.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='lazga_api.Type'),
        ),
    ]