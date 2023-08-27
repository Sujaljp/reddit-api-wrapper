from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('hot', views.getRoutesHot, name="routes"),
    path('new', views.getRoutesNew, name="routes"),
    path('top', views.getRoutesTop, name="routes"),
]
