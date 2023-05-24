from rest_framework import serializers
from .models import FifoModel, AvgBuyingPriceCal, StockHolder
class FifoModelSel(serializers.ModelSerializer):
    class Meta:
        model = FifoModel
        fields = ('__all__')
        
class AvgBuyigPriceCalSel(serializers.ModelSerializer):
    class Meta:
        model = AvgBuyingPriceCal
        fields = ('__all__')
        
class DetailedSel(serializers.Serializer):
    fifo_cal = serializers.SerializerMethodField()
    avg_buying_price_cal = serializers.SerializerMethodField()
    class Meta:
        fields = ('__all__')
        
    def get_fifo_cal(self,obj):
        try:
            data = FifoModelSel(FifoModel.objects.filter(user = obj),many=True).data
            return data
        except:
            pass
    def get_avg_buying_price_cal(self,obj):
        try:
            data = AvgBuyigPriceCalSel(AvgBuyingPriceCal.objects.get(user=obj)).data
            return data
        except:
            pass
        
class StockHolderSel(serializers.ModelSerializer):
    class Meta:
        model = StockHolder
        fields = ('__all__')
            