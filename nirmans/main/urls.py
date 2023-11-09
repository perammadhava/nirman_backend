from django.urls import path
from .views import AddService, VendorRegisterView, VendorLoginView,CustomerRegisterView,CustomerLoginView,CategoryList,ServiceList,ServiceDetail,VendorDetail,VendorList,CategoryDetail,AddService

urlpatterns = [
    path('vendor/register/', VendorRegisterView.as_view(), name='vendor-registration'),
    path('vendor/login/', VendorLoginView.as_view(), name='vendor-login'),

    path('customer/register/', CustomerRegisterView.as_view(), name='customer-registration'),
    path('customer/login/', CustomerLoginView.as_view(), name='customer-login'),


    path('vendors/',VendorList.as_view()),
    path('vendor/<int:pk>/',VendorDetail.as_view()),
   
    path('services/',ServiceList.as_view()),
    path('service/<int:pk>/', ServiceDetail.as_view()),
    path('addservice', AddService.as_view()),

    path('categories/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
   
]
