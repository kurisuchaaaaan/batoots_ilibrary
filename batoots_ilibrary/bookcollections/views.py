from django.shortcuts import render

from django.views.generic import TemplateView, ListView

#import Book model
from .models import Book

class BookListView(ListView):
    template_name = "book-list.html"
    model = Book

class BookDetailView(DetailView):
    template_name = "book-detail.html"
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context