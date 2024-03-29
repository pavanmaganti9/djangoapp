# Generated by Django 2.2.5 on 2019-10-12 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaults', '0006_auto_20191003_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('address', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 12, 23, 14, 4, 78733)),
        ),
    ]
