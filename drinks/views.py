from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request):

    if request.method == 'GET': 
       drinks = Drink.objects.all()
       serializer = DrinkSerializers(drinks,many=True)
       return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinkSerializers(data=(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id):

    drinks = Drink.objects.get(pk=id)

    if request.method == 'GET':
        seriazer = DrinkSerializers(drinks)
        return Response(seriazer.data)  

    elif request.method == 'PUT':
        seriazer = DrinkSerializers(drinks,data=request.data)
        if seriazer.is_valid():
            seriazer.save()
            return Response(seriazer.data)

    elif request.method == 'DELETE':
        drinks.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
