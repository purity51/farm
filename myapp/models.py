from django.db import models

# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    delivery = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    crops_order = models.TextField(blank=True)
    order_total = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.order_total}"