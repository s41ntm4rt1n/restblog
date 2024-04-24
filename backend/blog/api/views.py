from django.shortcuts import render
from django.http import JsonResponse
from articles.models import Article
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer
from rest_framework import generics

@api_view(['POST'])
def home(request, *args, **kwargs):
    serializer=ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)