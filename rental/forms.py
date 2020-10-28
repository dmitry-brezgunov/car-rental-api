from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count

from .models import Car, Rental, User


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'lang', )


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name_en', 'name_ru', 'creation_year', )


class RentCarForm(forms.ModelForm):
    cars = forms.ModelMultipleChoiceField(
        queryset=Car.objects.annotate(
            count=Count('rentals')).filter(count__lt=1))

    class Meta:
        model = Rental
        fields = ('cars', )
