"""View module for handling requests about comments"""

from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarerestapi.models import Comment, RareUser, Post
from datetime import datetime

class CommentView(ViewSet):
    """Rare-Rest Comment view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """
        comments = Comment.objects.all()
        post = request.query_params.get('post', None)
        if post is not None:
            comments = comments.filter(post=post)
        serializer = CommentSerializer(comments, many=True, context={'request':request} )
        return Response(serializer.data) 
    def create(self, request):
        """Handle POST operations for comments

        Returns:
            Response -- JSON serialized comment instance
        """
        post = Post.objects.get(pk=request.data['post'])
        author = RareUser.objects.get(user=request.auth.user)
        created_on = datetime.now().date()
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author, post=post, created_on=created_on)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """ 
        comment = Comment.objects.get(pk=pk)
        serializer = CreateCommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  
    
    def destroy(self, request, pk):              
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'created_on', 'content']
        depth = 2     

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post','author','created_on', 'content']

       
        
