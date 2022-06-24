from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=1000)

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    descriptions = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='movies', null=True)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

class Revieww(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True, default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text