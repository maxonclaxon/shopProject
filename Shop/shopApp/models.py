from django.db import models


class Center(models.Model):
    Name = models.CharField(max_length=128)
    Description = models.TextField()
    Address = models.CharField(max_length=256)


class Category(models.Model):
    Name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images/Categories/{0}/'.format(id))


class Shop(models.Model):
    Name = models.CharField(max_length=128)
    Description = models.TextField()
    Floor = models.PositiveIntegerField()
    Phone = models.CharField(max_length=32)
    ShopCenter = models.ForeignKey(Center, on_delete=models.CASCADE)
    Categories = models.ManyToManyField(Category)


class New(models.Model):
    Title = models.CharField(max_length=128)
    Description = models.TextField()
    date = models.DateTimeField()


def get_upload_image_filename(instance, filename):
    return'images/{0}/{1}/{2}'.format(instance.__class__.__name__, instance.id, filename)


class CenterImages(models.Model):
    image = models.ImageField(upload_to=get_upload_image_filename)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)


class NewImages(models.Model):
    image = models.ImageField(upload_to=get_upload_image_filename)
    new = models.ForeignKey(New, on_delete=models.CASCADE)


class ShopImages(models.Model):
    image = models.ImageField(upload_to=get_upload_image_filename)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


# Create your models here.
