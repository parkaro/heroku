from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment
