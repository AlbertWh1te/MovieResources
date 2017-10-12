# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import models

def index(request):
    movies_list = models.Movies.objects.all()
    paginator = Paginator(movies_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {"contacts": movies})