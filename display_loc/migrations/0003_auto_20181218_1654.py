# Generated by Django 2.1.4 on 2018-12-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display_loc', '0002_auto_20181218_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isslocation',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='isslocation',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
