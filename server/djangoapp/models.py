from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_est = models.IntegerField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('pickup', 'Pickup Truck'),
        ('convertible', 'Convertible'),
        ('minivan', 'Minivan'),
        ('crossover', 'Crossover'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    car_type = models.CharField(
        max_length=11,
        choices=CAR_TYPES,
        default='sedan',
    )
    year = models.IntegerField(
        default=2025,
        validators=[MaxValueValidator(2025), MinValueValidator(2015)],
    )

    def __str__(self):
        return self.name
