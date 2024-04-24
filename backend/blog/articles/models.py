from django.db import models

class Article(models.Model):
    category=models.CharField(max_length=255, blank=True, null=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255, blank=True, null=True)
    body=models.TextField()

    @property
    def content(self):
        return f'|Title: {self.title}| Author: {self.author}| Content: {self.body}|'