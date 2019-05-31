from django.shortcuts import render

from django.views.generic import ListView, DetailView

#import Book model
from .models import Book

class BookListView(ListView):
    template_name = "book-list.html"
    model = Book

class BookDetailView(DetailView):
    
    model = Book
   
    from django.shortcuts import get_object_or_404

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'templates/book-detail.html', context={'book': book})
    