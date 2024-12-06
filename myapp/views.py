from django.shortcuts import render
from .models import Customer, Product

# Create your views here.
def index(request):
    
    """
      products = Product.objects.all()
      variable = class/modelName.objects.all()
      this selects every object inside of the products class in models
      and assigns it to the varible of products
      same thing for customers, assigns every customer in the django db
      to the customers variable

    """

    products = Product.objects.all()
    customers = Customer.objects.all()

    """
      this renders index.html.
      in index.html, we have

      {% for product in products %}

      it checks
    """

    return render(request, 'myapp/index.html', {
        'products': products,
        'customer': customers
  })