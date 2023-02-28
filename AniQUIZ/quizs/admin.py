from django.contrib import admin
from . import models

admin.site.register(models.Quiz)
admin.site.register(models.Questions)
admin.site.register(models.cateory)
admin.site.register(models.Answers)
admin.site.register(models.Results)
admin.site.register(models.RatingStatus)