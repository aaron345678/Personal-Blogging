from rest_framework import serializers
from .models import Article, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(),source='tags',many=True,write_only=True,required=False)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'tags', 'tag_ids',
                  'published_at', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']