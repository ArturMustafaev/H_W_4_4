from django.contrib import admin
from main.models import Product ,Review, Movie, Director, Category, Tag, Revieww

# Register your models here.
class ReviewAdminInline(admin.StackedInline):
    model = Revieww
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = 'name tag_list category price is_active created_at updated_at'.split()
    search_fields = 'name descriptions '.split()
    list_filter = 'category tags is_active created_at'.split()
    list_editable = 'category price is_active'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_per_page = 3
    inlines = [ReviewAdminInline]

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = 'title descriptions director image'.split()
    search_fields = 'title'.split()
    list_filter = 'title director'.split()



admin.site.register(Product, ProductAdmin)
admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Revieww)
