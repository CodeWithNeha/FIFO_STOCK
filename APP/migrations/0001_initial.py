# Generated by Django 4.2.1 on 2023-05-23 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AvgBuyingPriceCal",
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
                ("total_buy_qty", models.FloatField()),
                ("total_sell_qty", models.FloatField()),
                ("closing_qty", models.FloatField()),
                ("closing_value", models.FloatField()),
                ("avg_buying_price", models.FloatField()),
            ],
            options={"db_table": "avg_buing_Price_cal",},
        ),
        migrations.CreateModel(
            name="FifoModel",
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
                ("date", models.DateField()),
                ("company_name", models.CharField(max_length=200)),
                ("trade_type", models.CharField(max_length=200)),
                ("quantity", models.FloatField()),
                ("buy_price", models.FloatField()),
                ("cummulative_cal", models.FloatField()),
                ("lot_pending_qty", models.FloatField(blank=True, null=True)),
                ("lot_value", models.FloatField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "fifo_model",},
        ),
    ]
