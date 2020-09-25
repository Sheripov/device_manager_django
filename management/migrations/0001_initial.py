# Generated by Django 3.1.1 on 2020-09-25 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=50, unique=True, verbose_name='Buyer Name')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=50, unique=True, verbose_name='Device type')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True, verbose_name='Team Name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('user_photo', models.ImageField(upload_to='user_photos/', verbose_name='User Photo')),
                ('employee_date', models.DateField(auto_now=True, verbose_name='Employee date')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('item_number', models.AutoField(primary_key=True, serialize=False, verbose_name='Item number')),
                ('device_name', models.CharField(max_length=50, verbose_name='Device Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('purchase_date', models.DateField(auto_now=True, verbose_name='Purchase_date')),
                ('configuration', models.URLField(verbose_name='URL for configuration')),
                ('device_photo', models.ImageField(upload_to='device_photos/', verbose_name='Device Photo')),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.devicetype')),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.buyer')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.team')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('assignment_date', models.DateField(auto_now=True, verbose_name='Assignment date')),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='management.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.user')),
            ],
        ),
    ]