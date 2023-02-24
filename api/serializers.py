from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers

from blog.models import Article


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            'id': obj.author.id,
            'username': obj.author.username,
            'first_name': obj.author.first_name,
            'last_name': obj.author.last_name,
        }

    author = serializers.SerializerMethodField('get_author')

    class Meta:
        model = Article
        fields = '__all__'

    def validate_title(self, value):
        filter_list = ['javascript', 'laravel', 'php']

        for word in filter_list:
            if word in value:
                raise serializers.ValidationError(f'dont use {word} in title')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
