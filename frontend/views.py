from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.core import paginator
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http.response import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpRequest
from datetime import datetime,date



import requests,sys


def home(request):
    return render(request,'home')