from django.shortcuts import render
from .models import Item
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import ItemSerializer, UserCreateSerializer, ItemCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

####################################################################

################
# There's a DRF generic view called a ListCreateAPIView
# You can use it to combine these and simplify your URLs
################


class ItemsList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCreateView(CreateAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

####################################################################


################
# There's a DRF generic view called a RetrieveUpdateDestroyAPIView
# You can use it to combine these and simplify your URLs
################
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
####################################################################
