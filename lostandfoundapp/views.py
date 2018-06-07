from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
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


class LostAndFoundCreateView(CreateView):
    model = LostAndFound
    fields = [f.name for f in LostAndFound._meta.get_fields()]
    fields.remove('author')
    fields.remove('author_email')
    template_name = "lostandfoundapp/add-post.html"
    SuccessMessageMixin = '%(title)s added successfully.'
    success_url = '/lostandfoundapp/'

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        form.instance.author_email = self.request.user.email
        return super(LostAndFoundCreateView, self).form_valid(form)


class LostAndFoundUpdateView(UpdateView):
    model = LostAndFound
    fields = [f.name for f in LostAndFound._meta.get_fields()]
    fields.remove('author')
    fields.remove('author_email')
    template_name = "lostandfoundapp/update-post.html"
    SuccessMessageMixin = '%(title)s updated successfully.'
    success_url = '/lostandfoundapp/'


class LostAndFoundDeleteView(DeleteView):
    model = LostAndFound
    template_name = "lostandfoundapp/delete-post.html"
    SuccessMessageMixin = '%(title)s deleted successfully.'
    success_url = '/lostandfoundapp/'


"""
To Display user's own Posts
"""

class UserLostAndFoundListView(ListView):
    model = LostAndFound
    template_name = "lostandfoundapp/my-posts.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super(UserLostAndFoundListView, self).get_queryset()
        queryset = queryset.filter(author_email = self.request.user.email)
        return queryset








        
    
