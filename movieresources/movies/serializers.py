# -*- coding: utf-8 -*-
from rest_framework import serializers
from movies import models


class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Movies
        fields = ("name","link","create_date")
   