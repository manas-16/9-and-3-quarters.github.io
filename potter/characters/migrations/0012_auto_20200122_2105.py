# Generated by Django 2.2.7 on 2020-01-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_book_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='synopsis',
            field=models.CharField(default='op', max_length=2000),
        ),
    ]