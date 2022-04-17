from .serializers import BookRegistrationSerializer, BookGenresSerializer
from .models import BookRegistration, BookGenres
from rest_framework.viewsets import ModelViewSet


    
class BookRegistrationMVS(ModelViewSet):
    queryset = BookRegistration.objects.all()
    serializer_class = BookRegistrationSerializer

class BookGenresMVS(ModelViewSet):
    queryset = BookGenres.objects.all()
    serializer_class = BookGenresSerializer