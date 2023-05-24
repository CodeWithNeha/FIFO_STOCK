from django.db import models

# model for fifo calculation raw data
class FifoModel(models.Model):
    user = models.CharField(max_length=120) #as i don't have any referrence for right now so im taing user variable so you can create entry by ur unique ref for now
    date = models.DateField()
    company_name = models.CharField(max_length=200)
    trade_type = models.CharField(max_length=200)
    quantity = models.FloatField()
    buy_price = models.FloatField()
    amount = models.FloatField()
    cummulative_cal = models.FloatField(null=True, blank=True)
    lot_pending_qty = models.FloatField(null=True,blank=True)
    lot_value = models.FloatField(null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "fifo_model"

# model for avgbuyingpricecal, here im assuming that we are gonna calculate data of single sheet
# if there are multiple users then we can store the data on behalf of user id
# and introduce foreign key so Primary key of user's table act as foreign key in these both the tables
class AvgBuyingPriceCal(models.Model):
    user = models.CharField(max_length=120) #as i don't have any referrence for right now so im taing user variable so you can create entry by ur unique ref for now
    total_buy_qty = models.FloatField()
    total_sell_qty = models.FloatField()
    closing_qty = models.FloatField()
    closing_value = models.FloatField()
    avg_buying_price = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "avg_buing_Price_cal"
        
        
class StockHolder(models.Model):
    user = models.CharField(max_length=120)
    shares_pre_split = models.IntegerField()
    stock_split_ratio = models.CharField(max_length=10)
    shares_post_split = models.IntegerField(blank=True, null=True)
    total_amount_invested = models.FloatField( blank=True, null=True)
    avg_buy_price_post_split = models.FloatField( blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "stock_split_cal"