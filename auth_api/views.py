from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from auth_api.models import Aspnetusers
from auth_api.procedures import RunLoginValidations
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

from auth_api.serializers import AspnetusersSerializer

# Create your views here.
def index(request):
    user = Aspnetusers.objects.filter(pk="00000322-F15A-496B-80BC-8A3B0483EEED").get()
    return HttpResponse(user.username)

@csrf_exempt
@api_view(['POST', 'GET'])
def auth_token(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AspnetusersSerializer(data=data)
        if serializer.is_valid():
            #serializer.save()
            print(RunLoginValidations("hola"))
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)