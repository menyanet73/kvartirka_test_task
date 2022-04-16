from rest_framework import serializers

from articles.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'