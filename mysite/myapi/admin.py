from django.contrib import admin
from .models import user, bank
#imports the models needed for the admin panel

# Register your models here.
admin.site.register(user)

admin.site.register(bank)
# could be cleaner in a model admin class
#TODO Research the admin model view
