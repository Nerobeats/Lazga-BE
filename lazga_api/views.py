from django.shortcuts import render
from .models import Item
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView,DestroyAPIView
from .serializers import ItemListSerializer, UserCreateSerializer, ItemCreateSerializer, ItemUpdateSerializer, ItemDetailSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser

class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemsList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class ItemCreateView(CreateAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'


class ItemUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Item.objects.all()
    serializer_class = ItemUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'

class DeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
