from django.shortcuts import render
from .models import Item, Order, OrderItem,Type, Profile
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import ItemSerializer, UserCreateSerializer, ItemCreateSerializer, OrderSerializer,TypeSerializer,OrderListSerializer,ProfileSerializer
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
            product_obj = Item.objects.get(id=product_id)
            type = Type.objects.filter(id= product_obj.type)
            product_obj.selling_counter = product_obj.selling_counter + int(quantity)
            productItem = OrderItem.objects.create(
                order=order_obj, item=product_obj, quantity=quantity)
            if (type.color):
                productItem.color = order.get('color')
            if (type.size):
                productItem.size = order.get('size')
            if (type.magic):
                productItem.magic = order.get('magic')
        return Response(status=status.HTTP_201_CREATED)


class OrdersList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    def get_queryset(self):
        return (Order.objects.filter(user = self.request.user))


class OrderUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'
    def get_queryset(self):
        if(request.user.IsAdminUser):
            return (Order.objects.all())
        return (Order.objects.filter(user = self.request.user))


class OrderDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsNotSubmitted]
    # Count the user orders (cart)             ^^
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'


class ProfilesList(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfilesUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated , IsAdminUser]
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'
    def get_queryset(self):
        if(request.user.IsAdminUser):
            return (Profile.objects.all())
        return (Profile.objects.filter(user = self.request.user))


class DeleteProfileView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'