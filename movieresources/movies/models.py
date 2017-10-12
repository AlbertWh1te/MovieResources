# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movies(models.Model):
    create_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    link = models.TextField()

    def __unicode__(self):
        return str(self.name)
    class Meta:
       ordering = ['-create_date']