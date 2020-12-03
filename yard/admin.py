from django.contrib import admin
from .models import Location, Yard, Time
# Register your models here.

class TimeLine(admin.TabularInline):
    model = Time
    extra = 5

class YardAdmin(admin.ModelAdmin):
    list_display = ["code", "location_id"]
    inlines = [TimeLine]

admin.site.register(Location)
admin.site.register(Yard, YardAdmin)
