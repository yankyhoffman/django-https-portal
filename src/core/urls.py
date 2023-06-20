from django.urls import include, path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('clear/', views.clear, name='clear'),
]
