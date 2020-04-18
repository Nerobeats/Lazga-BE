from django.shortcuts import render
from .models import Item, Order, OrderItem,Type
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import ItemSerializer, UserCreateSerializer, ItemCreateSerializer, OrderSerializer,TypeSerializer,OrderListSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .permissions import IsNotSubmitted
class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ItemsList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TypesList(ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ItemCreateView(CreateAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'


class ItemUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Item.objects.all()
    serializer_class = ItemCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'


class DeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'


class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        order_obj = Order.objects.create(
            user=request.user, totalPrice=request.data.get("totalPrice"))
        for order in request.data.get("products"):
            product_id = order.get('item')
            quantity = order.get('quantity')
            size = order.get('size')
            color = order.get('color')
            product_obj = Item.objects.get(id=product_id)
            productItem = OrderItem.objects.create(
                order=order_obj, item=product_obj, size=size, color=color, quantity=quantity)
        return Response(status=status.HTTP_201_CREATED)


class OrdersList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'


class OrderUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'


class OrderDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsNotSubmitted]
    # Count the user orders (cart)             ^^
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'
