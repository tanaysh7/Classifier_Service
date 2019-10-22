# from django.shortcuts import render
from django.http import JsonResponse
import requests
import model

def home(request):
    #response = requests.get('http://freegeoip.net/json/')
    #geodata = response.json()
    return JsonResponse({
    "glossary": {
        "title": "example glossary"
        }
        })