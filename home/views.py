
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import FileResponse
import os
def index(request):
    return render(request, 'home/index.html')
def upload(request):
    return render(request,'home/upload.html')
def hehe(request):
    return render(request,'home/hehe.html')