# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from movies import  models, spider, utils, serializers

# DRF
from rest_framework import generics,pagination

class ExamplePagination(pagination.PageNumberPagination):       
       page_size = 10

def first_init(n):
    for i in range(30000,n):
        info = spider.number_to_info(i)
        print(info)
        if info and not info.hasNone():
            duplicate = len(models.Movies.objects.filter(name=info['name']))
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
    return render_to_response('index.html', {"movies": movies})	

class MoviePagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class MovieListView(generics.ListAPIView):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializers
    pagination_class =  MoviePagination

class SearchListView(generics.ListAPIView):
    serializer_class = serializers.MoviesSerializers
    pagination_class =  MoviePagination

    def get_queryset(self):
        queryset = []
        name = self.request.query_params.get('name')
        if name:
            queryset = models.Movies.objects.filter(name__contains=name)
        return queryset

def init(requests):
    first_init(900000)
    movies_list = models.Movies.objects.all()
    return render_to_response('index.html', {"movies": movies_list})	
