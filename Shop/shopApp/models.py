from django.db import models

class Center(models.Model):
    id = models.AutoField()
    Name = models.CharField(max_length=128)
    Address = models.CharField(max_length=256)


class Category(models.Model):
    id = models.AutoField()
    Name = models.CharField(max_length=32)


class Shop(models.Model):
    id = models.AutoField()
    Name = models.CharField(max_length=128)
    Floor = models.PositiveIntegerField()
    Phone = models.CharField(max_length=32)
    ShopCenter = models.ForeignKey(Center, on_delete=models.CASCADE)
    Categoryes = models.ForeignKey(Category, on_delete=models.CASCADE)

class New(models.Model):
    id = models.AutoField()
    Title = models.CharField(max_length=128)
    Description = models.TextField()
    date = models.DateTimeField()





# Create your models here.
