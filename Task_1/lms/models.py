from django.db import models

# define your models here...
class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    date_published = models.DateField()
    author = models.OneToOneField('Author',on_delete=models.CASCADE,related_name="book")
    libraries = models.ForeignKey('Library',on_delete=models.CASCADE, related_name="book")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.DateField()
    books = models.ForeignKey('Book',on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.first_name + self.last_name
    

class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    data_established = models.DateField
    books = models.ForeignKey('Book',on_delete=models.CASCADE, related_name="library")
    def __str__(self):
        return self.name