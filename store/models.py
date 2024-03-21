from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phone_images/')
    
    def __str__(self):
        return f"{self.brand} {self.model_name}"

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.full_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/product_images/')
    camera = models.CharField(max_length=100)
    storage_ram = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    android_version = models.CharField(max_length=100)
    sim_type = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)