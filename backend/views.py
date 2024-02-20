from django.http import JsonResponse
from .models import UserPost, Opportunity
from .serializers import UserPostSerializer, OpportunitySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def post_list(request):

    if request.method == 'GET':
        posts = UserPost.objects.all()
        serializer = UserPostSerializer(posts, many = True)
        return JsonResponse(serializer.data, safe = False)
    if request.method == 'POST':
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def posts_detail(request,id):

    try:
        post = UserPost.objects.get(pk=id)
    except UserPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserPostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserPostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def opportunity_list(request):

    if request.method == 'GET':
        posts = Opportunity.objects.all()
        serializer = OpportunitySerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = OpportunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def opportunity_detail(request,id):

    try:
        post = Opportunity.objects.get(pk=id)
    except Opportunity.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OpportunitySerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OpportunitySerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)