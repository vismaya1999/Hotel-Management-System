from django.contrib import admin

# Register your models here.
from hostelapp import models

admin.site.register(models.Login)
admin.site.register(models.student)
admin.site.register(models.parent)