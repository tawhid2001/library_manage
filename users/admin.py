from django.contrib import admin
from .models import UserAddress,UserLibraryAccount

# Register your models here.


admin.site.register(UserLibraryAccount)
admin.site.register(UserAddress)