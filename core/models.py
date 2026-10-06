from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
        ('laptop', 'Laptop'),
        ('accessoire', 'Accessoire'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=100)
    price_usd = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Prix ($)")
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    stock = models.IntegerField(default=10)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.brand}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('delivered', 'Livrée'),
    )
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    commune = models.CharField(max_length=100)
    address_details = models.TextField()
    total_price_usd = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Commande #{self.id} - {self.full_name} ({self.commune})"