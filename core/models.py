from django.db import models
from tourist_attraction.models import TouristAttraction
from comments.models import Comment
from assessment.models import Assessment
from address.models import Address


class TouristSpot(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    tourist_attraction = models.ManyToManyField(TouristAttraction)
    comments = models.ManyToManyField(Comment)
    assessment = models.ManyToManyField(Assessment)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
