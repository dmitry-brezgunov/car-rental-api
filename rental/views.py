from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import AddCarForm, RentCarForm, UserRegisterForm
from .models import User
from .utils import rent_car_email


def index(request):
    return render(request, "index.html")


class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class AddCar(LoginRequiredMixin, CreateView):
    form_class = AddCarForm
    success_url = reverse_lazy("index")
    template_name = "addcar.html"


class AddRent(LoginRequiredMixin, CreateView):
    form_class = RentCarForm
    success_url = reverse_lazy("index")
    template_name = "addrent.html"

    def form_valid(self, form):
        rent = form.save(commit=False)
        rent.user = self.request.user
        rent.save()
        rent_car_email(self.request, form)
        return super().form_valid(form)


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile.html"

    def get_object(self):
        return self.request.user


class UserEdit(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'email', 'lang', )
    success_url = reverse_lazy("profile")
    template_name = "profile-edit.html"

    def get_object(self):
        return self.request.user
