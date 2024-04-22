from django.shortcuts import render
import requests

# Create your views here.
def indexpage(request):
    return render(request , "index.html")

def sportspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    response = url.json()
    sportsnews = response["data"]
    context = {
        "sportsnews":sportsnews
    }
    return render(request , "sports.html" , context)

def politicspage(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    response = url.json()
    politicsnews = response["data"]
    context = {
        "politicsnews" : politicsnews
    }
    return render(request , "politics.html" , context)