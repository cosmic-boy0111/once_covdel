from django.db import models
from datetime import date

# Create your models here.

class Registration(models.Model):
    person_id = models.AutoField
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50 , default='name')
    password = models.CharField(max_length=20)
    DOB = models.DateField()
    image = models.ImageField(upload_to='customer/img', default="")
    email = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    product_category = models.CharField(max_length=50, default="")
    product_subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    published = models.DateField()
    product_price_per_unit = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=5 , default='kg')
    mfg_date = models.DateField(default=date.today)
    expiry_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="customer/img", default="")

    def __str__(self):
        return self.product_name

