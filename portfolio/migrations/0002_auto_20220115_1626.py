# Generated by Django 3.0 on 2022-01-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]