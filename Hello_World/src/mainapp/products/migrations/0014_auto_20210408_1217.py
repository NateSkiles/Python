# Generated by Django 3.1.7 on 2021-04-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210408_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]
