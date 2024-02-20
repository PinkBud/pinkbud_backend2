from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import ChatModel
from backend.models import Therapist, User
# Create your views here.
import jwt
import datetime
VIDEOSDK_API_KEY = "30dc3932-3129-402f-a45c-367f20ca03e2"
VIDEOSDK_SECRET_KEY = "670b03d7783f79ee25631b6595a42f765121f15e288cfc66bb33637668369df0"
@api_view(['GET'])
def create_connection(request,email):
    th=Therapist.objects.get(email=email)
    a=ChatModel(administrator=th)
    a.save()
    expiration_in_seconds = 7200
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=expiration_in_seconds)

    token = jwt.encode(payload={
        'exp': expiration,
        'apikey': VIDEOSDK_API_KEY,
        'permissions': ['allow_join'], # 'ask_join' || 'allow_mod' 
        'version': 2, #OPTIONAL
    'roomId': f'{a.id}', #OPTIONAL 
	'participantId': f'{th.id}', #OPTIONAL
	#'roles': ['crawler', 'rtc'], #OPTIONAL 
    }, key=VIDEOSDK_SECRET_KEY, algorithm= 'HS256')
    print(token)
    a.token=token
    a.save()

    url = "https://api.videosdk.live/v2/rooms"
    headers = {'Authorization' : a.token,'Content-Type' : 'application/json'}
    response = requests.request("POST", url,json = {"region" : "sg001"},headers = headers)
    print(response.json()["roomId"])
    a.roomID=response.json()["roomId"]
    a.save()
    return Response({
        'token':token,
    })
@api_view(['GET'])
def join_room(request,email,id):
    us=User.objects.get(email=email)
    th=Therapist.objects.get(id=id)
    a=ChatModel.objects.get(administrator__id=th.id)
    roomId = a.roomID
    url = "https://api.videosdk.live/v2/rooms/validate/" + str(roomId)
    headers = {'Authorization' : a.token,'Content-Type' : 'application/json'}
    response = requests.request("GET", url,headers = headers)
    print(response.text)
    return Response({"room":response.json()["links"]["get_room"],"token":a.token})
@api_view(['GET'])
def leave_room(request,roomId):

    try:
        ChatModel.objects.get(roomId=roomId).delete()
        return Response({
            'status':'success'
        })
    except:
        return Response({
            'status':'failed'
        })
    
@api_view(['GET'])
def get_token(request):

    expiration_in_seconds = 7200
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=expiration_in_seconds)

    token = jwt.encode(payload={
        'exp': expiration,
        'apikey': VIDEOSDK_API_KEY,
        'permissions': ['allow_join'], # 'ask_join' || 'allow_mod' 
        'version': 2, #OPTIONAL
    }, key=VIDEOSDK_SECRET_KEY, algorithm= 'HS256')
    return Response({
        'token':token,
    })
