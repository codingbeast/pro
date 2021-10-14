from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def fail(request):
    print('fail has been called')
    return Response('Your call was successful', content_type='text/plain', status=status.HTTP_200_OK)

