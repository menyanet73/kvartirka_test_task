from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class CommentManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().prefetch_related('children')
                .order_by('created'))


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Comment(MPTTModel):
    author = models.CharField(max_length=50)
    text = models.TextField()
    # level = models.IntegerField(default=1)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )
    created = models.DateTimeField(auto_now_add=True)
    objects = CommentManager()

    def __str__(self) -> str:
        return self.author + ' ' + self.text[:10]

    @property
    def less_three(self):
        return self.objects.filter(level=3)
