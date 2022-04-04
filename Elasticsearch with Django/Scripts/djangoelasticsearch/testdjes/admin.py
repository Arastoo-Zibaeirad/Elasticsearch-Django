from django.contrib import admin
from .models import Home, Customer


class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    list_display_links = ['name']
    

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'budget']
    list_display_links = ['budget']
    
admin.site.register(Home, HomeAdmin)
admin.site.register(Customer, CustomerAdmin)