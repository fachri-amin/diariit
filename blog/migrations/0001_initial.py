# Generated by Django 2.2.4 on 2019-08-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('publish', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]