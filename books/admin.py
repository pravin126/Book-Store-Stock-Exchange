from django.contrib import admin

from .models import Book,Contact,Product

admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(Product)