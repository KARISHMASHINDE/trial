from django.shortcuts import render
from BlogPost.models import Tag,Posts
from BlogPost.serializers import RegistrationSerializer,PostsSerializer,TagSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import authentication,permissions

# Create your views here.


@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			user= serializer.save(request.user)
			data['response'] = 'successfully registered new user.'
			data['email'] = user.email
			data['username'] = user.username
		else:
			data = serializer.errors
		return Response(data) 



class PoststList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        obj = Posts.objects.all()
        serializer = PostsSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class PostsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PostsSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PostsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        
        obj = get_object_or_404(Posts, slug=slug)
       
        user = self.request.user
        updated = False
        clap = False
        if user.is_authenticated():
            if user in obj.claps.all():
                clap = False
                obj.claps.remove(user)
            else:
                clap = True
                obj.claps.add(user)
            updated = True
        data = {
            "updated": updated,
            "clap": clap
        }
        return Response(data)