from django.shortcuts import render
from ipware.ip import get_ip

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lineo.ip.models import Visit
from lineo.ip.serializers import VisitSerializer


@api_view(['GET', 'POST'])
def ips(request):
    """
    List all recorded ip addresses, or create a new one.
    """
    if request.method == 'GET':
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VisitSerializer(data={'ip_address': get_ip(request)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
