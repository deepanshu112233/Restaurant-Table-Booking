# Generated by Django 4.1.2 on 2022-11-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_restaurant_host_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
