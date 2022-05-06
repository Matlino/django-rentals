from django.db import models


class Rental(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()

    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=["checkin"])]
        ordering = ["checkin"]

