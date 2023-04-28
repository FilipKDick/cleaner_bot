from django.contrib import admin

from . import models


class ChoreHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('finished_at',)
    fields = ('chore', 'finished_at')


admin.site.register(models.ChorePage)
admin.site.register(models.ChoreGroup)
admin.site.register(models.Chore)
admin.site.register(models.ChoreHistory, ChoreHistoryAdmin)
