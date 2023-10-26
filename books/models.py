from django.db import models

# Create your models here.
class Book(models.Model):
    booktitle=models.CharField(max_length=50)
    boodetails=models.CharField(max_length=100)
    bookauthor=models.CharField(max_length=50)
    bookimage=models.ImageField(upload_to='images/')
    bookpath=models.FileField(upload_to='book_path/')

class Contact(models.Model):
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    contact_type=models.CharField(max_length=20)


    def __str__(self):
        return self.booktitle
        return self.boodetails
        return self.bookauthor