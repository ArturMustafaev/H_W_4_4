from django import forms
from main.models import Product, Movie, Director


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name description price is_active category tags'.split()
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название товара'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание товара'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену товара'
            }),
            'is_active': forms.CheckboxInput(attrs={
                # 'class': 'form-control'
            }),
            'category': forms.Select(attrs={
               'class': 'form-control',
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            })
        }


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title descriptions director'.split()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма'
            }),
            'descriptions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание фильма'
            }),
            'director': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = 'name'.split()
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя режиссера'
            })
        }