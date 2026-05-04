from django.contrib import admin
from .models import Ligne, Bus, Horaire

admin.site.register(Ligne)
admin.site.register(Bus)
admin.site.register(Horaire)
