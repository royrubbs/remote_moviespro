from django.db import models

class TeluguMovieApp(models.Model):
    Director_name=models.CharField(max_length=50)
    Hero_name=models.CharField(max_length=50)
    Heroin_name=models.CharField(max_length=50)
    Producer_name=models.CharField(max_length=50)
    Release_dt=models.DateTimeField()

class HindiMovieApp(models.Model):
    Director_name=models.CharField(max_length=50)
    Hero_name=models.CharField(max_length=50)
    Heroin_name=models.CharField(max_length=50)
    Producer_name=models.CharField(max_length=50)
    Release_dt=models.DateTimeField()

class EnglishMovieApp(models.Model):
    Director_name=models.CharField(max_length=50)
    Hero_name=models.CharField(max_length=50)
    Heroin_name=models.CharField(max_length=50)
    Producer_name=models.CharField(max_length=50)
    Release_dt=models.DateTimeField()

