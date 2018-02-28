from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path('indextwo', views.indextwo, name="indextwo"),
    path('getPrice', views.getPrice, name="getPrice")
]
