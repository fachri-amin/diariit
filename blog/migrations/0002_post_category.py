# Generated by Django 2.2.4 on 2019-08-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='no-category', max_length=100),
        ),
    ]
