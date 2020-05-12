from rest_framework import serializers
from blog.models import Post
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content','date_posted']
