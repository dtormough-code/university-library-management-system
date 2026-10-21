

from django.shortcuts import render
from .models import Book

def home(request):
    search = request.GET.get('search', '')

    books = Book.objects.all()

    if search:
        books = books.filter(title__icontains=search) | books.filter(author__icontains=search) | books.filter(isbn__icontains=search)

    context = {
        'books': books,
        'total_books': sum(book.quantity for book in Book.objects.all()),
        'available_books': sum(book.available_copies for book in Book.objects.all()),
        'total_titles': Book.objects.count(),
        'search': search,
    }

    return render(request, 'library/home.html', context)
