from rest_framework import routers

from order.viewset import OrderViewSet

urlpatterns = []
__author__ = "root"
router = routers.SimpleRouter()

router.register("order", OrderViewSet, basename="OrderViewSet")

urlpatterns += router.urls
