from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from models import Customer
from serializers import CustomerSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def customer(request):
    return JsonResponse({1:1})
