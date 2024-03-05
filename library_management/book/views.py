from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'library/index.html', {'form': form, 'books': books})