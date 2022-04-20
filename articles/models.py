from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    level = models.IntegerField(default=1)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name='children'
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author
