# Generated by Django 2.1.4 on 2018-12-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display_loc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isslocation',
            name='latitude',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='isslocation',
            name='longitude',
            field=models.CharField(max_length=10),
        ),
    ]
