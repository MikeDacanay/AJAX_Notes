# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index( request ):
    return render(request, "first_app/index.html")

def title(request):
	print request.POST['title_form']
	return redirect('/')