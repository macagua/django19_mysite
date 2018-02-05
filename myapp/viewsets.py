# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from myapp.models.blog import Post, Comment
from myapp.models.core import UserProfile
from myapp.serializers import PostSerializer, CommentSerializer
from mysite.serializers import UserProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    # This view automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # detail_route decorator stands for single instances, using pk element in its URL pattern
    @detail_route(methods=['POST'])
    def set_comment(self, request, pk=None):

        # get post object
        my_post = self.get_object()  
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=my_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
