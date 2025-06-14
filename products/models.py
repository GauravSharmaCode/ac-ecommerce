from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=200, blank=True)
    stock_status = models.BooleanField(default=True)
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        Returns the product's name as a string representation of the object.
        """
        
        return self.name
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
# This code defines a Django model for a product in an e-commerce application.
# The model includes fields for the product's name, price, description, category, tags, stock status, image, and timestamps for creation and updates.
# The `__str__` method returns the product's name for easy identification in the admin interface.
# The `Meta` class specifies the verbose names and ordering for the model.
# This model can be used to create, read, update, and delete product records in the database.