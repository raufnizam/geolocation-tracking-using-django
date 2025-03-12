from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    point = models.PointField(geography=True)  # Stores latitude & longitude
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.point}"
