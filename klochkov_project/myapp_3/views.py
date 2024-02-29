from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


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
