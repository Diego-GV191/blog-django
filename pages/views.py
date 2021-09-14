from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def page(request, url_amgable):

    page = Page.objects.get(slug=url_amgable)

    return render(request, 'pages/page.html', {
        'page': page # retorna datos a pages.html
    })