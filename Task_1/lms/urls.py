from django.urls import path
from . import views
urlpatterns = [
    path('',views.books_view, name = "books_list"),
    path('fetch_books/', views.fetch_books, name='fetch_books'),
]
