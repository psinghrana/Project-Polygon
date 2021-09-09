from django.contrib import admin
from Home.models import Provider
from Home.models import Services

# Register your models here.

admin.site.register(Provider)
admin.site.register(Services)
