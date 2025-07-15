# Uncomment the following imports before adding the Model code

# from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.description[:30]}"

# Car Model model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
    ]

    name = models.CharField(max_length=100, null=False)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES, default=SEDAN)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    dealer_id = models.IntegerField()

    def __str__(self):
        return f"{self.car_make.name} - {self.name} ({self.car_type}, {self.year})"
