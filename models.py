from django.db import models


class Registration(models.Model):
    person_id = models.AutoField
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    DOB = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    email = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=300)


class Product(models.Model):
    product_id = models.CharField(primary_key=1, max_length=20)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField()
    unit=models.CharField(max_length=5)
    mfg_date=models.DateField()
    expiry_date=models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
