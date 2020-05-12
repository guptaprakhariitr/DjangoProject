from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from blog.models import Post,User
from blog.api.serializers import BlogPostSerializer

@api_view(['GET',])
def api_detail(request):
    
    try:
        snippets = Post.objects.all()
        serializer = BlogPostSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
@api_view(['PUT',])
def api_update(request,pk):
    try:
        post = Post.objects.get(pk=request.pk)
        serializer = BlogPostSerializer(post,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Updated"
            return Response(data = data)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE',])
def api_delete(request):
    try:
        post = Post.objects.get(pk=request.pk)
        operation = post.delete()
        data= {}
        if operation:
            data["success"] = "DELETED"
            return Response(data = data)
    except Post.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
@api_view(['POST',])
def api_create(request):
    account = User.objects.get(pk=1)
    blog_post = Post(author = account)
    serializer = BlogPostSerializer(blog_post,data=request.data)
    if serializer.is_valid():
        serializer.save()                                                  
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

