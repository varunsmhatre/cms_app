from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .models import Post
from django.core.serializers import serialize
import json
from rest_framework.views import APIView
from .serializers import PostSerializer
from django.db.models import Q

def home(request):
    serialized_data = serialize("json", Post.objects.all())
    serialized_data = json.loads(serialized_data)
    content = {'posts': serialized_data}
    return JsonResponse(content)

class PostCreateView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'Post Created Successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        search_query = request.data.get('search')
        posts = Post.objects.all()
        posts = posts.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query) | Q(summary__icontains=search_query))
        serializer = PostSerializer(posts, many=True)
        return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)





# class PostListView(APIView):
#     def post(self, request, format=None):
#         serializer = UserRegistrationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token = get_tokens_for_user(user)
#         return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
