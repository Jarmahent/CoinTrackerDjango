from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path('pinance', views.get_value, name="coin"),
    path(r'indextwo', views.indextwo, name="indextwo"),
    path('updateData', views.updateData, name="updateData")
]
