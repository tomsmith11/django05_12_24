from django.contrib import admin
from .models import Customer, Product

# Register your models here.


"""
  this section defines how the information will be displayed on the admin
  page. for example, list_display defines which rows will be displayed on the
  main admin info db page.
"""

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_created')
    list_filter = ('date_created')

"""
  this does the same but for products on the admin view.
"""

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    list_filter = ('price')

