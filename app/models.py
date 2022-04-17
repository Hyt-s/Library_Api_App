from django.db import models

class BookGenres(models.Model):
    genre_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.genre_name

class BookRegistration(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=100)
    
    STATUS = [
        ("AV", "Available"),
        ("NA", "Not-Available"),
        ("RE", "Reserved"),
        ("SP", "Special"),
        ("OT", "Other"),
    ]
    book_status = models.CharField(max_length=50, choices=STATUS, default="AV")
    genre = models.ForeignKey(BookGenres, related_name="genres", on_delete=models.CASCADE)
    location_number = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.book_name} - {self.author}"
