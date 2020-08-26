from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post
from .serializers import PostSerializer


def index(request):
    return render(request, 'index.html', {})


def get_post(request):
    post_list = Post.objects.all()
    serialize = PostSerializer(post_list, many=True)
    print(serialize.data)
    return JsonResponse(serialize.data, safe=False)

