from django.urls import path
from .views import user_form, many_fields_from

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_from, name='many_fields_form'),
]
