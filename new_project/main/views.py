from django.shortcuts import render
from main.models import Product, Category, Director, Movie, Review, Tag, Revieww

# Create your views here.

def index(request):
    dict_={
        'key': "Hello World",
        'color': '#05fc89',
        'list_': ['Artur', 'Django', 'Python']
    }
    return render(request, 'index.html', context=dict_)



def product_list_view(request):
    context = {
        'product_list': Product.objects.all(),
        'category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', context={'product': product,
                                                   'category_list': Category.objects.all(),
                                                   'reviews': Revieww.objects.filter(product=product)})


def director_films(request):
    director = Director.objects.all()
    context = {
        'director_list': director
    }
    return render(request, 'Films.html', context=context)


def director_film(request, id):
    director = Director.objects.get(id=id)
    return render(request, 'director.html', context={'director': director})


def movies_film(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'director': director_films
    }
    return render(request, 'film.html', context=context)


def movies_films(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie.html', context={'movie': movie,
                                                  'director': director_films})


def review(request):
    review = Review.objects.all()
    context = {
        'review_list': review
    }
    return render(request, 'review.html', context=context)


def review_list(request, id):
    review = Movie.objects.get(id=id)
    return render(request, 'rewiev_.html', context={'review': review})


def category_product_filter_view(request, category_id):
    context = {
        'product_list': Product.objects.filter(category_id=category_id),
        'category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)