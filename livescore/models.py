from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.




class Batsman(models.Model):
    name = models.ForeignKey('auth.User')
    character = models.CharField(max_length=200)
    style = models.TextField()
    playing_date = models.DateTimeField(
            default=timezone.now)
    Out_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.uut_date = timezone.now()
        self.save()

    def __str__(self):
        return self.style
