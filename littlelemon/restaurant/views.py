from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import generics, viewsets  
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Menu , Booking
from .serializers import MenuSerializer , UserSerializer, BookingSerializer

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):  
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer