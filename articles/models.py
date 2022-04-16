from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Comment(MPTTModel):
    author = models.CharField(max_length=50)
    text = models.TextField()
    level = models.IntegerField()
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def __str__(self) -> str:
        return self.author