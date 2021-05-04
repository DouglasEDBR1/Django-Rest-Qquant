from django.db import models

class TouristAttraction(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    opening_hours = models.TextField()
    minimum_age = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
