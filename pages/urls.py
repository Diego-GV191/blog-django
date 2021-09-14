from django.urls import path
from . import views

urlpatterns = [
    path('pagina/<str:url_amgable>', views.page, name='page' )
]
