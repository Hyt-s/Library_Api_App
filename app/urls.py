from django.urls import path, include
from .views import BookRegistrationMVS, BookGenresMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookRegistrationMVS)
router.register('genres', BookGenresMVS)

urlpatterns = [
    path('', include(router.urls))
]