from django.shortcuts import get_object_or_404
from rental.models import Car, User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CarSerializer, UserSerializer


class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'success': 'Вы успешно зарегистрированны'},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    page_size = 10

    @action(detail=True, methods=['get'])
    def cars(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        cars = Car.objects.filter(rentals__user=user)
        page = self.paginate_queryset(cars)
        serializer = CarSerializer(
            page, many=True, context={'request': request})
        return self.get_paginated_response(serializer.data)
