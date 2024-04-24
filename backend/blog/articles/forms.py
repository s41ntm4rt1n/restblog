from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=[
            'category', 
            'title', 
            'author', 
            'body',
        ]