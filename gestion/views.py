from django.shortcuts import render
from .models import Ligne, Horaire, Bus

# الصفحة الرئيسية (اختياري)
def home(request):
    Lignes =Ligne.objects.all()
    Horaires = Horaire.objects.all()


    return render(request, 'gestion/home.html',{
         'Lignes': Lignes,
        'Horaires': Horaires

            })
     