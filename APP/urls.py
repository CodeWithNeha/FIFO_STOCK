
from django.urls import path
from rest_framework import routers
from .views import FifoDataManageView, CalculateStockSplit

router = routers.DefaultRouter()
router.register(r'fifoDataManage', FifoDataManageView)
router.register(r'stockSplitManage',CalculateStockSplit)
# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls