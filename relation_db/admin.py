from django.contrib import admin

from . import models

admin.site.register(models.NumberCar)
admin.site.register(models.DocumentCar)
admin.site.register(models.Review)
admin.site.register(models.Tag)
# Register your models here.
