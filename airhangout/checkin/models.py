from django.db import models

class Checkin(models.Model):
    question = models.CharField(max_length=200)