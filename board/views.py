from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import BoardSerializer, Board

# Create your views here.
@api_view(['GET'])
def board_details(request,**shaun):
    # board = Board.objects.all() 
    board = None
    if 'pk' in shaun:
        board = BoardSerializer(Board.objects.get(pk=shaun['pk']), many=False).data
    else:
        board = BoardSerializer(Board.objects.all(), many=True).data
    
    return Response(board)

@api_view(['POST'])
def board_actions(request):
    board = None
    if request.method == 'POST':
        # board = Board.objects.create(
        #     title = request.data['title'],
        #     description = request.data['description'],
        # )
        serializers = BoardSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()

    return Response(serializers.data)