from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Book
        fields = [
            'id', 
            'name', 
            'category', 
            'created_by', 
            'created_by_id',
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        # Set created_by to the current user if not provided
        if 'created_by_id' not in validated_data:
            validated_data['created_by'] = self.context['request'].user
        else:
            validated_data['created_by_id'] = validated_data.pop('created_by_id')
        return super().create(validated_data)


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'category']
        
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
