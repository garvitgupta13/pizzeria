from typing import Any

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from order.service import OrderService


class OrderViewSet(viewsets.ViewSet):
    """
    Viewset to handle all order related operations
    """

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.order_service = OrderService

    @action(detail=False, methods=["post"], url_path="create")
    def process_single_order(self, request):
        """
        Process single order

        :param request:
        :return: HTTP Response
        """
        order_id = self.order_service.generate_order_id()
        OrderService.create_order(order_id)
        return Response()

    @action(detail=False, methods=["post"], url_path="bulk-create")
    def process_bulk_order(self, request):
        """
        Process bulk orders

        :param request:
        :return: HTTP Response
        """
        order_cnt = request.data["order_cnt"]
        for _ in range(order_cnt):
            order_id = self.order_service.generate_order_id()
            OrderService.create_order(order_id)
        return Response()
