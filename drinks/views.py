from django.http import JsonResponse
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
       serializer = DrinkSerializers(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
       

@api_view(['GET','POST','PUT','DELETE'])
def drink_details(request,id): 
   
   drinks = Drink.objects.get(pk=id)

   if request.method == 'GET':
      serializers=DrinkSerializers(drinks)
      return Response(serializers.data)
   
   elif request.method == 'POST':
      pass    
   
   elif request.method == 'PUT':
      serializers=DrinkSerializers(drinks,data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data)
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
   
   elif request.method == 'DELETE':
      drinks.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)