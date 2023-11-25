from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=11)
    booking_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, №{self.no_of_guests}"



class Menu(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField(max_length=5)


    def __str__(self):
        return f"{self.title}"