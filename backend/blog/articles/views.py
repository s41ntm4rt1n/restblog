from rest_framework import generics
from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
    def perform_create(self, serializer):
        
        title=serializer.validated_data.get('title')
        body=serializer.validated_data.get('body') or None
        if body in None:
            body = title
        serializer.save(body=body)
    

class ArticleDetailView(generics.RetrieveAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    
    
class ArticleUpdateView(generics.UpdateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.body:
            instance.body=instance.title
        
    
# class ArticleDeleteView(generics.DeleteAPIView):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer
