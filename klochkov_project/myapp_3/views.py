from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from .models import Author, Post
# Create your views here.


def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello world from class!")


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp_3/my_template.html", context)


class TemplIf(TemplateView):
    template_name = "myapp_3/templ_if.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello world!!!"
        context['number'] = 5
        return context


def view_for(requast):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }

    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(requast, 'myapp_3/templ_for.html', context)


def index(request):
    return render(request, 'myapp_3/index.html')


def about(request):
    return render(request, 'myapp_3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp_3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp_3/post_full.html', {'post': post})
