from django.contrib import admin
from .models import Product,ProductImage,Category,Product_Accessories,Product_Altrnative
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Accessories)
admin.site.register(Product_Altrnative)