from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=[
            'category', 
            'title', 
            'author', 
            'body',
            'content'
        ]