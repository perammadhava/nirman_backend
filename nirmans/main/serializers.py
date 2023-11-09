# vendors/serializers.py
from rest_framework import serializers
from .models import Vendor,Customer,Service,serviceCategory
from rest_framework import generics

class VendorSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Vendor
        fields = ('id', 'first_name', 'last_name', 'username', 'email' ,'phone_number','password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  # Remove 'confirm_password' from validated data
        user = Vendor(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class VendorLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id','first_name','username', 'phone_number')

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id','first_name','username', 'phone_number') 

                # use depth to fetch user data
    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1       

class CustomerSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'username', 'email' ,'phone_number','password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  # Remove 'confirm_password' from validated data
        user = Vendor(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(write_only=True)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=serviceCategory
        # which fields we want to show
        fields=['id','title','detail']

        # use depth to fetch user data
    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1


#create CategoryDetailSerializer and extend the model Serializer
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=serviceCategory
        # which fields we want to show
        fields=['id','title','detail']

        # use depth to fetch user data
    def __init__(self, *args, **kwargs):
        super(CategoryDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1


class AddServiceSerializer(serializers.ModelSerializer):
    #product_ratings=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Service
        # which fields we want to show, coming from product model
        fields=['id','category','vendor', 'title', 'description', 'price_per_day','price_per_hour','price_per_sq_feet','price_per_service','tags','location','contact_number',]

        # use depth to fetch user data
    def __init__(self, *args, **kwargs):
        super(AddServiceSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1        


class ServiceListSerializer(serializers.ModelSerializer):
    #product_ratings=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Service
        # which fields we want to show, coming from product model
        fields=['id', 'title','vendor' ]

        # use depth to fetch user data
    def __init__(self, *args, **kwargs):
        super(ServiceListSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1


#create ProductDetailSerializer and fileds will be same as product list
class ServiceDetailSerializer(serializers.ModelSerializer):
    #product_ratings=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=Service
        # which fields we want to show, coming from product model
        fields=['id','category','vendor', 'title', 'description', 'price_per_day','price_per_hour','price_per_sq_feet','price_per_service','tags','location','contact_number','images']

        # use 1depth to fetch user data
    def __init__(self, *args, **kwargs):
        super(ServiceDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth =1

