from django.contrib import admin

from .models import Car, User, Rental


admin.site.register(Car)
admin.site.register(User)
admin.site.register(Rental)
