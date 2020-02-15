from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Entry
from django.db import models


class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3
# Create your views here.

class EntryView(DetailView):
    model = Entry 
    template_name = 'entries/entry_detail.html'
    

    # We use this function to incerase number of views at webpage
    def get(self, *args, **kwargs):
        pk = self.kwargs['pk'] # We get pk for that object
        EntryParams = Entry.objects.get(pk = pk)
        EntryParams.entry_nViews += 1
        EntryParams.save()
        context = super(EntryView, self).get(*args, **kwargs)
        return context



class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = {'entry_title','entry_text'}
    

    def form_valid(self,form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

class AboutMeView(TemplateView):
    model = Entry
    template_name = 'entries/aboutMeView.html'
