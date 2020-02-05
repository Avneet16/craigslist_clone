from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.
def home(request):
    return render(request,'base.html')

def search(request):
    new_search=request.POST.get('search')
    stuff_for_frontend={'search':new_search}
    return render(request, 'my_app/new_search.html',stuff_for_frontend)