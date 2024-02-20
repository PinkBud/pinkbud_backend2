from .serializers import UserSerializer
from .serializers import TherapistSerializer
from .serializers import NgoSerializer
from .serializers import LawyerSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .models import Therapist
from .models import Lawyer
from .models import Ngo

@api_view(['GET','POST'])
def user_sign_up(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            response_data = {
                'success':True,
                'details':user_data
            }
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse({'error':'Invalid user data', 'errors':serializer.errors}, status = 400)
    else:
        return JsonResponse({'error':'Invalid request method'}, status=400)

@api_view(['GET','POST'])
def therapist_sign_up(request, format=None):
    if request.method == 'GET':
        users = Therapist.objects.all()
        serializer = TherapistSerializer(users, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TherapistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            response_data = {
                'success': True,
                'details': user_data
            }
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@api_view(['GET', 'POST'])
def lawyer_sign_up(request, format=None):
    if request.method == 'GET':
        users = Lawyer.objects.all()
        serializer = LawyerSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LawyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            response_data = {
                'success': True,
                'details': user_data
            }
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@api_view(['GET', 'POST'])
def ngo_sign_up(request, format=None):
    if request.method == 'GET':
        users = Ngo.objects.all()
        serializer = NgoSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NgoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            response_data = {
                'success': True,
                'details': user_data
            }
            return JsonResponse(response_data, status=201)
        else:
            return JsonResponse({'error': 'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)