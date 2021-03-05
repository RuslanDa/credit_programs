from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Offer, Checklist
from .serializers import OfferSerializer, ChecklistSerializer


@api_view(['GET', 'POST'])
def check_list(request, partner_id):
    """
    List all checklits, or create a new checklist.
    """
    if request.method == 'GET':
        chklists = Checklist.objects.filter(partner=partner_id)
        serializer = ChecklistSerializer(chklists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChecklistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def chklist_detail(request, partner_id, chklst_id):
    """
    Retrieve, update or delete a checklist.
    """
    try:
        chklist = Checklist.objects.get(id=chklst_id, partner=partner_id)
    except Checklist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChecklistSerializer(chklist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChecklistSerializer(chklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        chklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
