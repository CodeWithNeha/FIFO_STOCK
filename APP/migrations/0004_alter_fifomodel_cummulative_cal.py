# Generated by Django 4.2.1 on 2023-05-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("APP", "0003_avgbuyingpricecal_user_fifomodel_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fifomodel",
            name="cummulative_cal",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
