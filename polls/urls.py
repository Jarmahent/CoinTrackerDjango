from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path('pynance', views.get_value, name="coin"),
    path('indextwo', views.indextwo, name="indextwo"),
    path('getPrice', views.getPrice, name="getPrice")
]
