from django.contrib import admin

# Register your models here.
from .models import *



@admin.register(Product)
class ProductCategoryAdmin(admin.ModelAdmin):
        list_display = [
        'product_sub_category','sku','product_name','slug','main_category','description','unit_price','created_date','modified_date'
        ]
        prepopulated_fields = {'slug': ('sku','product_name',)}
        # list_filter = ['is_active','record_status','modified_date']
        
@admin.register(SubProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
        list_display = ['product','sub_product_totel_stoke','offerprice','offer_expiry_date','offer_stoke','is_active']

@admin.register(SubProductAttributeImages)
class ProductAttributeImagesAdmin(admin.ModelAdmin):
        list_display = ['product_attribute','title','images']



@admin.register(ProductQuantity)
class ProductQuantityAdmin(admin.ModelAdmin):
        list_display = ['product','quantity','is_active']

