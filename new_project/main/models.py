from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

class Tag(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')
    name = models.CharField(max_length=1000, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена (в долларах)')
    quantity = models.IntegerField(verbose_name='Колличество')
    is_active = models.BooleanField(default=True, verbose_name='Активен?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='products', null=True, verbose_name='Картинка')

    def __str__(self):
        return self.name

    @property
    def tag_list(self):
        return ', '.join([tag.name for tag in self.tags.all()])

class Director(models.Model):
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
    name = models.CharField(max_length=1000, verbose_name='Режиссер')

class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=1000)
    descriptions = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='movies', null=True)


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

class Revieww(models.Model):
    class Meta:
        verbose_name = 'Отзыв на товар'
        verbose_name_plural = 'Отзыв на товары'
    text = models.TextField(verbose_name='Отзывы')
    author = models.CharField(max_length=100, null=True, blank=True, default="", verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews', verbose_name='Товар')

    def __str__(self):
        return self.text