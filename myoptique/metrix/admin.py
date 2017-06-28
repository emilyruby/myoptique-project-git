from django.contrib import admin

from myoptique.metrix.models import Department, Metric


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    list_editable = ('name', 'department')

admin.site.register(Department)
