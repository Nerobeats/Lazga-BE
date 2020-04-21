from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item, Order, OrderItem,Type,Profile


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
        Profile.objects.create(user = new_user)
        Order.objects.create(user = new_user)
        return validated_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        
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
    products = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = ['user']

class OrderListSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'
    def get_products(self, obj):
        return (OrderItemSerializer(OrderItem.objects.filter(order=obj),many =True).data)


class OrderSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status"]


class ProfileSerializer(serializers.ModelSerializer):
    favorites = ItemSerializer(many=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user', 'favorites']

