# Generated by Django 2.2.7 on 2020-01-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0017_movie_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='movies', verbose_name='Movie'),
        ),
    ]