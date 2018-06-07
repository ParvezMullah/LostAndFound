"""lostandfound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.urls import reverse
from django.conf import settings
from .views import (
                    LostAndFoundListView, 
                    LostAndFoundDetailView,
                    LostAndFoundCreateView,
                    LostAndFoundUpdateView,
                    LostAndFoundDeleteView,
                    UserLostAndFoundListView,

                    )

app_name = 'lostandfoundapp'
urlpatterns = [
    path('', LostAndFoundListView.as_view(), name = 'home'),
    path('detail/<int:pk>/<slug:slug>/', LostAndFoundDetailView.as_view(), name = 'detail'),
    path('add/', LostAndFoundCreateView.as_view(), name = 'add' ),
    path('update/<int:pk>/<slug:slug>/', LostAndFoundUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/<slug:slug>/',LostAndFoundDeleteView.as_view(), name = 'delete'),
    path('myposts/', UserLostAndFoundListView.as_view(), name = 'myposts')

]

