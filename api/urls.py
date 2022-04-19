from django.urls import include, path
from rest_framework import routers

from api import views


router = routers.SimpleRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'articles/(?P<article_id>\d+)/comments',
                views.CommentViewset,
                basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
