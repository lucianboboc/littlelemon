from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f'{self.name} : {self.booking_date}'


class Booking(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : ${str(self.price)}'
