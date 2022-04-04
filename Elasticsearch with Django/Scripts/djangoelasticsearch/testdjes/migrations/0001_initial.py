# Generated by Django 3.2 on 2022-01-17 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField()),
                ('square_meter', models.SmallIntegerField()),
                ('property_type', models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('Flat', 'Flat'), ('Dublex', 'Dublex')], max_length=100, null=True)),
                ('doc_type', models.CharField(choices=[('original', 'original'), ('gholname', 'gholname')], max_length=100)),
                ('age', models.IntegerField()),
                ('parking', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('telephone', models.BooleanField(default=False)),
                ('warehouse', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('terrace', models.BooleanField(default=False)),
                ('price', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('budget', models.BigIntegerField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testdjes.home')),
            ],
        ),
    ]
