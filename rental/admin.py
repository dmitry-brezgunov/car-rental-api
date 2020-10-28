from django.contrib import admin

from .models import Car, Rental, User

admin.site.register(Car)
admin.site.register(User)
admin.site.register(Rental)
