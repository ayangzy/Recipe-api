from pyexpat import model
from django.contrib import admin
from core import models

# Register your models here.

admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
