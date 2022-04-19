from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from articles.models import Article, Comment
from api.viewsets import CreateDeleteListViewset
from api.serializers import ArticleSerializer, CommentSerializer


class ArticleViewSet(CreateDeleteListViewset):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewset(CreateDeleteListViewset):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        queryset = Comment.objects.filter(article=article_id, level__lte=3)
        return queryset

    def perform_create(self, serializer):
        article_id = self.kwargs.get('article_id')
        article = get_object_or_404(Article, pk=article_id)
        serializer.save(level=1, article=article, parent=None)

    @action(methods=['post'], detail=True, url_path='reply')
    def reply_comment(self, request, article_id, pk):
        article = get_object_or_404(Article, pk=article_id)
        parent = get_object_or_404(Comment, pk=pk)
        level = parent.level + 1
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(article=article, parent=parent, level=level)
        return Response(serializer.data)
