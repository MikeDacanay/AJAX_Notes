# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index( request ):
    return render(request, "first_app/index.html")

def title(request):
	Notes.objects.create(title=request.POST['title_form'])
	notes= Notes.objects.all()
	return render(request, "first_app/add.html", {'notes':notes})

def delete(request):
	Notes.objects.get(id=request.POST['hid_id_form']).delete()
	notes= Notes.objects.all()
	return render(request, "first_app/add.html", {'notes':notes})

def texter(request):
	print request.POST['textarea']
	test=Notes.objects.get(id=request.POST['id'])
	test.note=request.POST['textarea']
	test.save()
	return redirect('/')