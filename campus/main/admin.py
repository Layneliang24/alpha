from django.contrib import admin
from main import models

admin.site.register(models.MainCategory)
admin.site.register(models.SubCategory)
admin.site.register(models.Article)
admin.site.register(models.File)
admin.site.register(models.Link)
