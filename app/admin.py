from django.contrib import admin
from .models import BookRegistration, BookGenres

admin.site.register(BookRegistration)
admin.site.register(BookGenres)