from conda.common.configuration import CustomValidationError
from dask.dataframe.multi import required
from django.db import models
import datetime
# Create your models here.
#Category of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


#Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



#Products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=250,null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.TextField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name


#orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=250,default='',blank=True,null=True)
    phone = models.CharField(max_length=50,default='',blank=False,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} {self.quantity}'