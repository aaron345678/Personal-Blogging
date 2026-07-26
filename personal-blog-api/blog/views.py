from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-published_at')
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['tags__name','published_at']
    order_fields = ['published_at','created_at','title']