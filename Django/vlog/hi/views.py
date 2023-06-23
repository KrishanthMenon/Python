from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from hi.serializers import Postserializer
from rest_framework.viewsets import ModelViewSet
from hi.models import Post
import time

# Create your views here.
class HelloWorldView(APIView):

    def get(self, request):
        return Response({"info" : "Hello world!"})
        time.sleep(25)

class Postview(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer
