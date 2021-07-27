from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from . models import Post
from . serializers import postSerializers



from .models import Post


class postList(APIView):
    def get(self, request):
        posts1 = Post.objects.all()
        serializer=postSerializers(posts1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def home(request):
    data = Post.objects.all()
    return render(request, "index.html", {"posts":data})

def single(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, "single.html", {"post":data})

def aboutus(request):
    return render(request, "aboutus.html", {})

