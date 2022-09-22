from django.contrib import admin
from login import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.ConfirmString)
