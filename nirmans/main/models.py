# vendors/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Vendor(AbstractUser):
    # Fields you mentioned
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            ("can_view_sensitive_data", "Can view sensitive data"),
            # Add any custom permissions you need here
        ]

    # Use related_name to resolve the clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='vendors',
        related_query_name='vendor',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='vendors',
        related_query_name='vendor',
        blank=True,
    )


class Customer(AbstractUser):
    # Fields you mentioned
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            ("can_view_sensitive_data", "Can view sensitive data"),
            # Add any custom permissions you need here
        ]

    # Use related_name to resolve the clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customers',
        related_query_name='customer',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customers',
        related_query_name='customer',
        blank=True,
    )


class serviceCategory(models.Model):
    # whenevr you use charfiled the max length is compulsary
    title=models.CharField(max_length=200)
    # This details field can be null
    detail=models.TextField(null=True)

    # whenever we call this fuction it returns,this magic methog __str__, self.title
    def __str__(self):
        return self.title




class Service(models.Model):
    category=models.ForeignKey(serviceCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
    # Who is adding the product
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    price_per_service = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    price_per_sq_feet = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    tags=models.TextField(null=True)
    images = models.ImageField(upload_to='service_images/', blank=True, null=True)


       # whenever we call this fuction it returns,this magic methog __str__, self.title
    def __str__(self):
        return self.title 