# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from movies import  models,spider,utils

def first_init(n):
    for i in range(1,n):
        info = spider.number_to_info(i)
        print(info)
        if info and not info.hasNone():
            duplicate = models.Movies.objects.filter(name=info['name'])
            if not duplicate:
                movie = models.Movies(
                    name = info['name'],
                    link = info['link']
                )
                movie.save()

def index(request):
    movies_list = models.Movies.objects.all()
    paginator = Paginator(movies_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)



def init(requests):
    first_init(1000)
    return "done"
