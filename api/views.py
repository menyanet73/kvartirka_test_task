from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from articles.models import Article, Comment
from api.viewsets import CreateDeleteListViewset
from api import serializers


class ArticleViewSet(CreateDeleteListViewset):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class CommentViewset(CreateDeleteListViewset):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        queryset = Comment.objects.filter(article=article_id)
        return queryset

    def perform_create(self, serializer):
        article_id = self.kwargs.get('article_id')
        article = get_object_or_404(Article, pk=article_id)
        serializer.save(level=1, article=article, parent=None)

    def retrieve(self, *args, **kwargs):
        instance = self.get_object()
        serializer = serializers.CommentChildSerializer(instance)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, url_path='reply')
    def reply_comment(self, request, article_id, pk):
        article = get_object_or_404(Article, pk=article_id)
        parent = self.get_object()
        level = parent.level + 1
        serializer = serializers.CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(article=article, parent=parent, level=level)
        return Response(serializer.data)
