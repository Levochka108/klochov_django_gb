from django.urls import path
from .views import hello, HelloView
from .views import TemplIf
from .views import view_for
from .views import index, about
from .views import author_posts, post_full

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='idex'),
    path('about/', about, name='about'),
    path('author/<int:author_id>', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
