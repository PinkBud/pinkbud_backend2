from .models import User, Therapist, Lawyer, Ngo
from .serializers import TherapistSerializer, LawyerSerializer, NgoSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def login(request, format=None):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email, password=password)
            user_data = UserSerializer(user).data
        except User.DoesNotExist:
            try:
                therapist = Therapist.objects.get(email=email, password=password)
                therapist_data = TherapistSerializer(therapist).data
            except Therapist.DoesNotExist:
                try:
                    lawyer = Lawyer.objects.get(email=email, password=password)
                    lawyer_data = LawyerSerializer(lawyer).data
                except Lawyer.DoesNotExist:
                    try:
                        ngo = Ngo.objects.get(email=email, password=password)
                        ngo_data = NgoSerializer(ngo).data
                    except Ngo.DoesNotExist:
                        return JsonResponse({'error': 'Invalid username or password'}, status=400)

        response_data = {
            'success': True,
            'details': user_data if 'user_data' in locals() else therapist_data if 'therapist_data' in locals() else lawyer_data if 'lawyer_data' in locals() else ngo_data
        }
        return JsonResponse(response_data, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

