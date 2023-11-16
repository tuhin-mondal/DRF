from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.response import Response

@api_view(['GET'])
def drink_list(request):

    drinks = Drink.objects.all()
    serializer = DrinkSerializers(drinks,many=True)
    return Response(serializer.data)