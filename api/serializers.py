from rest_framework import serializers

from blog.settings import MAX_COMMENT_LEVEL
from articles.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Article


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if instance.level > MAX_COMMENT_LEVEL:
            return
        serializer = CommentSerializer(instance, context=self.context)
        return serializer.data


class CommentListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    children = RecursiveSerializer(many=True, required=False)
    all_comments_url = serializers.SerializerMethodField(read_only=True)

    def get_all_comments_url(self, obj):
        pass

    class Meta:
        list_serializer_class = CommentListSerializer
        model = Comment
        fields = (
            'id', 'article', 'author', 'text', 'level', 'parent', 'created',
            'children', 'all_comments_url',
        )


class RecursiveChildSerializer(RecursiveSerializer):

    def to_representation(self, instance):
        serializer = CommentChildSerializer(instance, context=self.context)
        return serializer.data


class CommentChildSerializer(CommentSerializer):
    children = RecursiveChildSerializer(many=True, required=False)
