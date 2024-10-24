from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('coucou', views.index, name='coucou'),
    path('truc', views.truc, name='truc'),
]
