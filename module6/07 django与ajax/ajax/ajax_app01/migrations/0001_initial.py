# Generated by Django 2.2.3 on 2019-08-12 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=32)),
                ('phone', models.BigIntegerField()),
                ('age', models.BigIntegerField()),
                ('address', models.CharField(max_length=32)),
                ('dep', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('user_detail',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ajax_app01.UserDetail')),
            ],
        ),
    ]
