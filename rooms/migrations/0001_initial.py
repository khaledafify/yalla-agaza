# Generated by Django 3.0 on 2020-06-21 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='e')),
                ('country', django_countries.fields.CountryField(default='EG', max_length=2)),
                ('city', models.CharField(default='', max_length=80)),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=5)),
                ('address', models.CharField(default='', max_length=255)),
                ('guests', models.IntegerField(default=0)),
                ('beds', models.IntegerField(default=1)),
                ('bedrooms', models.IntegerField(default=1)),
                ('baths', models.IntegerField(default=1)),
                ('check_in', models.TimeField(default=None)),
                ('check_out', models.TimeField(default=None)),
                ('instant_book', models.BooleanField(default=False)),
                ('host', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
