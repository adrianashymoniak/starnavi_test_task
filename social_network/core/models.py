from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    author = models.ForeignKey('auth.User', related_name='posts',
                               on_delete=models.CASCADE)
    likes = models.ManyToManyField('auth.User', blank=True)

    class Meta:
        ordering = ['created', ]

    def __str__(self):
        return self.title
