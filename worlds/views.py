from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import World

@csrf_exempt
def next_world(request):
    response = _cors_response()
    if request.method.lower() == 'options':
        return response
    else:
        live_cells = json.loads(request.body)['live_cells']
        world = World(live_cells).next_iteration()
        response.write(json.dumps( {'live_cells': world.live_cells()} ))
        return response

def _cors_response():
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization, Token'
    response.status_code = 200
    return response

