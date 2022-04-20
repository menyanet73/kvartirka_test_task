from rest_framework import serializers

from blog.settings import MAX_COMMENT_LEVEL
from articles.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Article


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, instance):
        serializer = CommentSerializer(instance, context=self.context)
        return serializer.data


class CommentListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    children = RecursiveSerializer(many=True, required=False)

    class Meta:
        list_serializer_class = CommentListSerializer
        model = Comment
        fields = (
            'id', 'article', 'author', 'text', 'level', 'parent', 'created',
            'children',
        )

    def to_representation(self, instance):
        if instance.get_level() == MAX_COMMENT_LEVEL:
            ret = super(CommentSerializer, self).to_representation(instance)
            ret.pop('children')
            url = (self.context.get('request').build_absolute_uri()
                   + str(instance.pk))
            ret['url'] = url
            return ret
        return super().to_representation(instance)


class RecursiveChildSerializer(RecursiveSerializer):

    def to_representation(self, instance):
        serializer = CommentChildSerializer(instance, context=self.context)
        return serializer.data


class CommentChildSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    children = RecursiveChildSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = (
            'id', 'article', 'author', 'text', 'level', 'parent', 'created',
            'children',
        )
