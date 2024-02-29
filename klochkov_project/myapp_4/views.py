import logging

from django.shortcuts import render
from .forms import UserFrom, ManyFieldsForm


logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            # Логирование полученных данных
            logger.info(f'Получили {name=}, {email=}, {age=}')
    else:
        form = UserFrom()
    return render(request, 'myapp_4/user_form.html', {'form': form})


def many_fields_from(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp_4/many_fileds_form.html', {'form': form})
