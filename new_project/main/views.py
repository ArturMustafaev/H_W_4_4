from django.shortcuts import render, redirect
from main.models import Product, Category, Director, Movie, Review, Tag, Revieww
from main.forms import ProductForm, MovieForm, DirectorForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

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


def add_product_view(request):
    form = ProductForm()
    if request.method == 'GET':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    return render(request, 'add_product.html', context={
        'form': form,
        'category_list': Category.objects.all()
    })

def add_movie_view(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request, 'add_movie.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movie/')
        return render(request, 'add_movie.html', context={
            'form': form
        })


def add_director_view(request):
    if request.method == 'GET':
        form = DirectorForm()
        return  render(request, 'add_director.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/directors/')
        return  render(request, 'add_director.html', context={
            'form': form
        })


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/')
    return render(request, 'register.html', context={
        'form': form
    })


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
        return redirect('/login/')
    return render(request, 'login.html', context={
        'form': form
    })
