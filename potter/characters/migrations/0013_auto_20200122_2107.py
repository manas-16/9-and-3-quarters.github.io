# Generated by Django 2.2.7 on 2020-01-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_auto_20200122_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='synopsis',
            field=models.CharField(default='op', max_length=3000),
        ),
    ]
