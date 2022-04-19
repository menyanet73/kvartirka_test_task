from rest_framework import serializers

from articles.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Article


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = (
            'id', 'article', 'author', 'text', 'level', 'parent', 'created'
        )
        model = Comment
