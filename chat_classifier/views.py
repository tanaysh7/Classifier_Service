# from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .model import predict



@csrf_exempt
def home(request):
    #response = requests.get('http://freegeoip.net/json/')
    #geodata = response.json()
    return JsonResponse({
    "dermalogica.com": {
        "name":"livechat-classifier",
        "version":"1.0.0"
        }
        })





@csrf_exempt
def predict_chat(request, chat_string):

    
	return JsonResponse(predict(chat_string))


    
