from django.db import models
from django.contrib.auth.models import User
from elasticsearch_dsl import Q

class Home(models.Model):
    user = models.ForeignKey(User, related_name='home', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.TextField()
    square_meter = models.SmallIntegerField()
    APARTMENT = "Apartment"
    FLAT = "Flat"
    DUBLEX = "Dublex"
    property_type_fields = (        
        (APARTMENT, "Apartment"),
        (FLAT, "Flat"),
        (DUBLEX, "Dublex"),
    )
    property_type = models.CharField(max_length=100, null=True, blank=True, choices=property_type_fields)
    ORIGINAL = "original"
    GHOLNAME = "gholname"
    doc_type_fields = (       
        (ORIGINAL, "original"),
        (GHOLNAME, "gholname"),
    )
    doc_type = models.CharField(max_length=100, choices=doc_type_fields)
    age = models.IntegerField()
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    telephone = models.BooleanField(default=False)
    warehouse = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    price = models.BigIntegerField()
    
    def __str__(self):
        return f"{self.name}"
    

class Customer(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    home = models.ForeignKey('Home', on_delete=models.CASCADE)
    budget = models.BigIntegerField()
    
    def __str__(self):
        return f"{self.budget}"
    