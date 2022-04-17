from rest_framework import serializers
from .models import BookRegistration, BookGenres


class BookGenresSerializer(serializers.ModelSerializer):    
    class Meta:
        model = BookGenres
        fields = "__all__"
        
class BookRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRegistration
        fields = ["id", "book_name", "book_description", "author", "publication_date", "publisher", "book_status", "genre", "location_number"]
