from django.contrib import admin
from main.models import Product ,Review, Movie, Director, Category, Tag, Revieww

# Register your models here.

admin.site.register(Product)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Revieww)
