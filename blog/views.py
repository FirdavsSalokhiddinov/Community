from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def requested_post(request, pk):
    post = Post.objects.get(id = pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)