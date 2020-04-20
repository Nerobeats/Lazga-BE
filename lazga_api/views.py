from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
ItemSerializer,
UserCreateSerializer,
ItemCreateSerializer,
OrderSerializer,
OrderItemSerializer,
TypeSerializer,
OrderListSerializer,
ProfileSerializer,
OrderSubmitSerializer,
ProfileUpdateSerializer
)

from .models import Item, Order, OrderItem,Type, Profile

from .permissions import IsNotSubmitted ,IsOwner

# -------------- Register -----------#
class RegisterView(CreateAPIView):
	serializer_class = UserCreateSerializer

#---------------ITEMS CRUD--------------------#
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


class DeleteItemView(DestroyAPIView):
	permission_classes = [IsAuthenticated, IsAdminUser]
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'

#---------------Order & OrderItem CRUD--------------------#

class OrderItemCreateView(APIView):
	permission_classes = [IsAuthenticated]
	def post(self, request, *args, **kwargs):
		order = Order.objects.get(user = self.request.user, status ="NS" )
		product_id = request.data.get('item')
		quantity = request.data.get('quantity')
		product_obj = Item.objects.get(id=product_id)
		type = Type.objects.get(id= product_obj.type.id)
		product_obj.selling_counter = product_obj.selling_counter + int(quantity)
		color = "N/A"
		size = "N/A"
		magic = False
		if (type.color):
		   color = request.data.get("color")
		if (type.size):
			size = request.data.get('size')
		if (type.magic):
			magic = request.data.get('magic')
		if product_obj in order.products.all():
			new_product = OrderItem.objects.create(order = order, item = product_obj , size = size , quantity = quantity , color = color , magic = magic)
		order.products.add(product_obj , through_defaults={"order" : order, "item" :product_obj,"quantity" : quantity,  "color": color, "size" : size , "magic" : magic})
		return Response(status=status.HTTP_201_CREATED)
		


class OrdersList(ListAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = OrderListSerializer
	def get_queryset(self):
		return (Order.objects.filter(user = self.request.user))

class SubmitOrder(UpdateAPIView):
	permissions = [IsOwner]
	serializer_class = OrderSubmitSerializer
	def get_object(self):
		order = Order.objects.get(user = self.request.user, status ="NS" )
		Order.objects.create(user = self.request.user , status = "NS")
		return (order)


class OrderUpdateView(UpdateAPIView):
	permission_classes = [IsAuthenticated, IsAdminUser]
	serializer_class = OrderSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'order_id'
	def get_queryset(self):
		if(request.user.IsAdminUser):
			return (Order.objects.all())
		return (Order.objects.filter(user = self.request.user))


class OrderItemDeleteView(DestroyAPIView):
	permission_classes = [IsAuthenticated, IsNotSubmitted]
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'orderitem_id'

#---------------Profile & Favorites CRUD--------------------#

class ProfilesList(ListAPIView):
	permission_classes = [IsAdminUser]
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class ProfileDetails(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'user_id'
	lookup_url_kwarg = 'profile_id'
	

class ProfileUpdate(UpdateAPIView):
   def put(self, request, profile_id, format=None):
	   profile = Profile.objects.get(user_id = profile_id)
	   serializer = ProfileUpdateSerializer(profile, data=request.data)
	   if serializer.is_valid():
		   serializer.save()
		   return Response(serializer.data)
	   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddToFavorites(UpdateAPIView):
	def put(self, request,format=None):
		profile = Profile.objects.get(user_id = request.user.id)
		item = Item.objects.get(id = request.data.get('item_id'))
		profile.favorites.add(item)
		return Response(status=status.HTTP_202_ACCEPTED)

class RemoveFavorite(UpdateAPIView):
	def put(self, request,format=None):
		profile = Profile.objects.get(user_id = request.user.id)
		item = Item.objects.get(id = request.data.get('item_id'))
		profile.favorites.remove(item)
		return Response(status=status.HTTP_202_ACCEPTED)
