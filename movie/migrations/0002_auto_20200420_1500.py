# Generated by Django 2.0 on 2020-04-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.AddField(
            model_name='movie',
            name='time',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='intro',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_time',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writers',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
