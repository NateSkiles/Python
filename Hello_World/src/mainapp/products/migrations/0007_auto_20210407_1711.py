# Generated by Django 3.1.7 on 2021-04-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210407_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
