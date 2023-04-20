import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from logica import users
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def index(request):
    nick_name = request.POST.get('nick_name')
    full_name = request.POST.get('full_name')

    try:
        user = users.create_user(nick_name=nick_name, full_name=full_name)
        response = {
            "status": "success",
            "code": 200,
            "data": "User saved successfully"
        }
    except Exception as e:
        response = {
            "status": "error",
            "code": 400,
            "data": str(e)
        }

    return JsonResponse(response)