from django.contrib import admin
from sim.models import Person

@admin.register(Person)
class PepytrsonAdmin(admin.ModelAdmin):
    pass