from django.db import models


class Ligne(models.Model):
    nom_ligne = models.CharField(max_length=50, unique=True) 
    point_depart = models.CharField(max_length=100)
    point_arrivee = models.CharField(max_length=100)
    duree_estimee = models.DurationField(help_text="الوقت التقريبي للرحلة")

    def __str__(self):
        return f"{self.nom_ligne} ({self.point_depart} -> {self.point_arrivee})"


class Bus(models.Model):
    number = models.CharField(max_length=50)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.number


class Horaire(models.Model):
    ligne = models.ForeignKey(Ligne, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)
    heure_depart = models.TimeField()
    heure_arrivee = models.TimeField()
    frequence = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ligne.nom_ligne} depart {self.heure_depart}"