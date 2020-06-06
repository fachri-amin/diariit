# Generated by Django 2.2.4 on 2019-09-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormDaftar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tanggal_lahir', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('alamat', models.TextField()),
                ('agree', models.BooleanField()),
            ],
        ),
    ]
