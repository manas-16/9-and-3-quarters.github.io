# Generated by Django 2.2.7 on 2020-01-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0021_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.CharField(default='1998', max_length=5),
        ),
    ]