# Generated by Django 2.2.3 on 2019-08-11 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables_app001', '0002_auto_20190811_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='sal',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
