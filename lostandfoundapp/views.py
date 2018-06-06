from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpRequest, HttpRequest
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import LostAndFound

# Create your views here.

class LostAndFoundListView(ListView):
    model = LostAndFound
    template_name = "lostandfoundapp/home.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super(LostAndFoundListView, self).get_queryset()
        search_text = self.request.GET.get('search', None)
        lostorfound = self.request.GET.get('lostorfound', None)
        if search_text != None and lostorfound != None:
            queryset = queryset.filter(lost_or_found= lostorfound, title__icontains=search_text)
        elif lostorfound != None:
            queryset = queryset.filter(lost_or_found= lostorfound)
        elif search_text!= None:
            queryset = queryset.filter(title__icontains=search_text)
        return queryset 

    


class LostAndFoundDetailView(DetailView):
    model = LostAndFound
    template_name = "lostandfoundapp/detail.html"




        
    
