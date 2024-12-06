from django.db import models

# Create your models here.

<<<<<<< HEAD
"""
  define Customer class with attributes of name, email, phone and date created
  models.Model means that this class is a model and django will create a table in the database for this model
"""

class Customer(models.Model): 
=======
class Customer(models.Model):
>>>>>>> origin/dev
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)

    """
      by defining name_and_email, we define a variable that is then displayed in def __str__
    """

    def name_and_emaiL(self):
        return f"{self.name} ({self.email})"

    """ 
        def __str__(self): defines what will be displayed as the title on django admin page, eg
        a product on the django admin page will consist of {self.name} and {self..price}
    """

    def __str__(self):
        return self.name_and_emaiL()
    

"""
  define Product class with attributes of name, price, and description
"""

=======
    def __str__(self):
        return f"{self.name} ({self.email})"
    
>>>>>>> origin/dev
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)

<<<<<<< HEAD
    """ 
        def __str__(self): defines what will be displayed as the title on django admin page, eg
        a product on the django admin page will consist of {self.name} and {self..price}
    """

    def __str__(self):
        return f"{self.name} ({self.price})" 
=======
    def __str__(self):
        return f"{self.name} ({self.price})"
>>>>>>> origin/dev
