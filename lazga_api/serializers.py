from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item

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

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'type', 'tags' , "image_url" , "id"]


class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'type', 'tags',"image_url"]


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'type', 'tags',"image_url"]



class ItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['name', 'description', 'type', 'tags',"image_url" , "id"]
