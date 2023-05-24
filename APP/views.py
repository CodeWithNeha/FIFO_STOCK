from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import FifoModel, AvgBuyingPriceCal, StockHolder
from django.db import transaction
from .EnumFile import *
import datetime
from .serializers import DetailedSel, StockHolderSel

# this class is for calculating fifo valuation
# FifoModel and AvgBuyingPriceCal are the model name and DetailedSel is serializer class
# only two types of method allowd in this class i.e. post and get 
# post method is for creating the db entry
# get method is for retrieving the entry from db
class FifoDataManageView(viewsets.ViewSet):
    queryset = FifoModel.objects
    subQueryset = AvgBuyingPriceCal.objects
    serializer_class = DetailedSel
    http_method_names = ['post','get']
    def create(self, request):
        try:

            request_data = request.data
            days_data = request_data['days_data'] # days_data is the array of objects provided by the frontend
            user = request_data['user'] 
            total_sell_qty = 0.00
            total_buy_qty = 0.00
            cummulative_cal = 0.00
            try:
                self.subQueryset.get(user=user)
                return Response({
                                "message":"Here we don't have any requirements regarding same user can add data multiple times."
                            },status = status.HTTP_400_BAD_REQUEST)
            except:
                pass
            with transaction.atomic(): # if there is any issue occur with one db entry during add data in db it will rollback the previous 
                for data in days_data:
                    try:
                        date = data['date'] # date format is as defined in the excel sheet and i'm changing this  below
                        company_name = data['company_name']
                        trade_type = data['trade_type']
                        qty = float(data['qty'])
                        buy_price = float(data['buy_price'])
                        amount = qty*buy_price
                    except KeyError as error:
                        error = str(error)
                        return Response({
                                "message":f"Please enter valid {error}  for date {date}."
                            },status = status.HTTP_400_BAD_REQUEST)
                    if trade_type == TRADE_TYPE.BUY:
                        total_buy_qty += qty
                    else:
                        total_sell_qty += qty
                closing_qty = total_buy_qty-total_sell_qty
                cummulative_cal = -total_sell_qty
                closing_value = 0.00
                for data in days_data:
                    date = datetime.datetime.strptime(data['date'],"%m/%d/%Y").strftime("%Y-%m-%d")# convert datetime format 
                    company_name = data['company_name']
                    trade_type = data['trade_type']
                    qty = float(data['qty'])
                    buy_price = float(data['buy_price'])
                    amount = qty*buy_price
                    if trade_type == TRADE_TYPE.BUY: # TRADE_TYPE.BUY is the enum
                        cummulative_cal += qty
                        data['cummulative_cal'] = cummulative_cal
                        data['lot_pending_qty'] = None if (cummulative_cal<0) else min(qty,cummulative_cal)
                        if data['lot_pending_qty']:
                            data['lot_value'] = data['lot_pending_qty']*buy_price
                            closing_value += data['lot_value']
                        else:
                            data['lot_value'] = None
                    else:
                        cummulative_cal = 0
                        data['cummulative_cal'] = None
                        data['lot_pending_qty'] = None
                        data['lot_value'] = None
                    self.queryset.create( # data added in FifoModel table 
                        date = date,
                        company_name = company_name,
                        trade_type = trade_type,
                        quantity = qty,
                        buy_price = buy_price,
                        amount = amount,
                        cummulative_cal = data['cummulative_cal'],
                        lot_pending_qty = data['lot_pending_qty'],
                        lot_value = data['lot_value'],
                        user = user
                    )
                avg_buying_price = closing_value/closing_qty
                self.subQueryset.create(   # data added in AvgBuyingPriceCal table
                    user = user,
                    total_buy_qty = total_buy_qty,
                    total_sell_qty = total_sell_qty,
                    closing_qty = closing_qty,
                    closing_value = closing_value,
                    avg_buying_price = avg_buying_price
                )
            return Response({
                "message":"Data added successfully."
            },status = status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self,request):
        try:
            serialized = self.serializer_class(request.GET.get('user')).data # serializer class will give the data of fifo model as well avg_buying_price_cal
            return Response({
                "data":serialized,
                "message":"Data fetched successfully."
            },status = status.HTTP_200_OK)

        except:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
# this class is for calculating stock split ratio
# StockHolder is My model name and StockHolderSel is serializer class
# only two types of method allowd in this class i.e. post and get 
# post method is for creating the db entry
# get method is for retrieving the entry from db
class CalculateStockSplit(viewsets.ViewSet):
    queryset = StockHolder.objects
    serializer_class = StockHolderSel
    http_method_names = ['post','get']
    def create(self,request):
        try:
            request_data = request.data
            try:
                user = request_data['user']
                try:
                    self.queryset.get(user=user)
                    return Response({
                                    "message":"Here we don't have any requirements regarding same user can add data multiple times."
                                },status = status.HTTP_400_BAD_REQUEST)
                except:
                    pass
                stock_split_ratio = request_data['stock_split_ratio']
                shares_pre_split = int(request_data['shares_pre_split'])
                total_amount_invested = int(request_data['total_amount_invested'])
            except KeyError as error:
                error = str(error)
                return Response({
                        "message":f"Please enter valid {error}."
                    },status = status.HTTP_400_BAD_REQUEST)

            split_ratio = stock_split_ratio.split(':')
            pre_split_qty = shares_pre_split
            print(int(split_ratio[0]))
            print((pre_split_qty * int(split_ratio[0])) / int(split_ratio[1]))
            post_split_qty = (pre_split_qty * int(split_ratio[0])) / int(split_ratio[1])

            if post_split_qty > 0:
                adjusted_avg_buy_price = total_amount_invested / post_split_qty
                shares_post_split = post_split_qty
                avg_buy_price_post_split = adjusted_avg_buy_price
            else:
                shares_post_split = None
                avg_buy_price_post_split = None
            self.queryset.create(
                user = user,
                shares_pre_split = shares_pre_split,
                stock_split_ratio = stock_split_ratio,
                shares_post_split = shares_post_split,
                total_amount_invested = total_amount_invested,
                avg_buy_price_post_split = avg_buy_price_post_split
            )
            return Response({
                "message":"Data added successfully."
            },status = status.HTTP_200_OK)   
        except Exception as error:
            print(error)
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def list(self,request):
        try:
            data = self.queryset.get(user = request.GET.get('user'))
            serialized = self.serializer_class(data).data
            return Response({
                "data":serialized,
                "message":"Data fetched successfully."
            },status = status.HTTP_200_OK)

        except:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
