from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT=((1,'Fashion'),(2,'Beauty and Grooming'),(3,'Healthcare'),(4,'Grocery'),(5,'Home and Furniture'),(6,'Toys and BabyCare'),(7,'Electronics'),(8,'Electronics'))
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    pdetail=models.CharField(max_length=300, verbose_name='Product Detail')
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Cart(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    amt=models.FloatField()
