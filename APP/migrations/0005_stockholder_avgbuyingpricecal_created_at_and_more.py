# Generated by Django 4.2.1 on 2023-05-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("APP", "0004_alter_fifomodel_cummulative_cal"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockHolder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=120)),
                ("shares_pre_split", models.IntegerField()),
                ("stock_split_ratio", models.CharField(max_length=10)),
                ("shares_post_split", models.IntegerField(blank=True, null=True)),
                ("total_amount_invested", models.FloatField(blank=True, null=True)),
                ("avg_buy_price_post_split", models.FloatField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "stock_split_cal",},
        ),
        migrations.AddField(
            model_name="avgbuyingpricecal",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="avgbuyingpricecal",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]