from django.urls import include, path

from . import views

urlpatterns = [
        path("signup/", views.SignUp.as_view(), name="signup"),
        path("", include("django.contrib.auth.urls")),
        path("", views.index, name="index"),
        path("addcar/", views.AddCar.as_view(), name="addcar"),
        path("addrent/", views.AddRent.as_view(), name="addrent"),
        path("profile/", views.UserProfile.as_view(), name="profile"),
        path("profile-edit/", views.UserEdit.as_view(), name="profile-edit"),
]
