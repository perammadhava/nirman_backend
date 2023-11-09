from django.contrib import admin
from .models import Vendor,Customer,serviceCategory,Service

# Register your models here.

admin.site.register(Vendor),
admin.site.register(Customer),
admin.site.register(serviceCategory),
admin.site.register(Service),
