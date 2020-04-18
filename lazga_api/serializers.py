from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item, Order, OrderItem,Type


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', "last_name", "email"]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.first_name = validated_data['first_name']
        new_user.last_name = validated_data['last_name']
        new_user.email = validated_data['email']
        new_user.save()
        return validated_data


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'type', 'tags', "image_url", "price"]


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        exclude = ['order']

    def get_item(self, obj):
        return (ItemSerializer(Item.objects.get(id=obj.item.id)).data)


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = ['user', 'products']

class OrderListSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
