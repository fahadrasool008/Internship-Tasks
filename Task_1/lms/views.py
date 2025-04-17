from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Book

def fetch_books(request):

    search = request.GET.get('search[value]','')
    order_column = int(request.GET.get('order[0][column]',0))
    order_dir = request.GET.get('order[0][dir]','asc')

    order_fields = ['id','title','author','date_published']
    order_by = order_fields[order_column] if order_column < len(order_fields) else 'id'

    books = Book.objects.select_related('author').prefetch_related('libraries').only().values('id','title','author__first_name','libraries__name','date_published').distinct().filter(
        Q(title__icontains = search)| Q(author__first_name__icontains = search)| Q(libraries__name__icontains = search)
    ).order_by(f'{order_by}' if order_dir == 'asc' else f'-{order_by}')


    draw = request.GET.get('draw', 1)
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    books_page = books[start:start + length]
    data = list(books_page)

    return JsonResponse({
        'draw': draw,
        'recordsTotal': Book.objects.count(), 
        'recordsFiltered': len(books),       
        'data': data,                        
    })

def books_view(request):
    return render(request,'index.html')