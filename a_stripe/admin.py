from django.contrib import admin
from .models import *

admin.site.register(ShippingInfo)
admin.site.register(CheckoutSession)

admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(ProductVariation)
admin.site.register(ProductVariationObject)



