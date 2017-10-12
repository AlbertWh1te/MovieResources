# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    template_name = "index.html"
    readonly_fields = ('create_date',)
    search_fields = ['name']
    list_display = ('name', 'create_date', 'link')


admin.site.register(models.Movies,MoviesAdmin)