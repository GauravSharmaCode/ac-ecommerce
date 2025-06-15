from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='clients_logos/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns the client's name as a string representation of the object.
        """
        
        return self.name
