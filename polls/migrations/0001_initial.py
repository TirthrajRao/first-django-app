# Generated by Django 2.2.6 on 2019-10-16 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='uploads')),
                ('content', models.TextField()),
                ('createdAt', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
