from django.contrib import admin

from . import models

admin.site.register(models.ChorePage)
admin.site.register(models.ChoreGroup)
admin.site.register(models.Chore)
