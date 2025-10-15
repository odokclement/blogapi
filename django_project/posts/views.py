from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
