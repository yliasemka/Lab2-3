from django.contrib import admin
from .models import *
from .models import Review

admin.site.register(Service)
#admin.site.register(CartProduct)
#admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Review)


