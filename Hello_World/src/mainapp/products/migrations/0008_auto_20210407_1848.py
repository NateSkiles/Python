# Generated by Django 3.1.7 on 2021-04-08 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210407_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]