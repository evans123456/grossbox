# Generated by Django 2.0.13 on 2019-07-26 19:47

import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biker',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id_number', models.IntegerField()),
                ('residence', models.CharField(max_length=80)),
                ('mobile_number', models.IntegerField()),
                ('vehiecle', models.CharField(choices=[('bicycle', 'Bicycle'), ('motor bike', 'Motor Bike')], max_length=20)),
                ('area_of_business', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Bikers',
            },
            bases=('auth.user',),
        ),
    ]
