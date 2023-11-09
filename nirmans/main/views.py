from django.shortcuts import render

# Create your views here.
# vendors/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Vendor,Customer,serviceCategory,Service
from .serializers import VendorSerializer,VendorLoginSerializer,CustomerSerializer,CustomerLoginSerializer,ServiceListSerializer,CategorySerializer,ServiceDetailSerializer,CategoryDetailSerializer,VendorListSerializer,VendorDetailSerializer,AddServiceSerializer

class VendorRegisterView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data)


    

class VendorLoginView(generics.CreateAPIView):
    serializer_class = VendorLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = Vendor.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=400)
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data)


class CustomerRegisterView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data)


    

class CustomerLoginView(generics.CreateAPIView):
    serializer_class = CustomerLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = Vendor.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=400)
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data)

class VendorList(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorListSerializer
    permission_classes = (permissions.AllowAny,)

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
    permission_classes = (permissions.AllowAny,)    



class AddService(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = AddServiceSerializer   


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer      




class CategoryList(generics.ListCreateAPIView):
    queryset = serviceCategory.objects.all()
    serializer_class = CategorySerializer


# category detail API view
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = serviceCategory.objects.all()
    serializer_class = CategoryDetailSerializer

  