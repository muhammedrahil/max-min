from django.contrib import admin

# Register your models here.

from .models import Category,SubCategory,Size,Brand



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        list_display = [
        'id','category','slug','is_active',
        'created_date', 'created_id','created_ip','modified_date','modified_id','modified_ip','record_status'
        ]
        prepopulated_fields = {'slug': ('category',)}
        list_filter = ['is_active','record_status','modified_date']



@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
        list_display = [
        'category','sub_category','slug','is_active',
        # 'created_date', 'created_id','created_ip','modified_date','modified_id','modified_ip','record_status'
        ]
        prepopulated_fields = {'slug': ('sub_category',)}
        # list_filter = ['is_active','record_status','modified_date']



@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
        list_display = [
        'category','Size','slug','discription','is_active',
        # 'created_date','created_id','created_ip','modified_date','modified_id','modified_ip','record_status'
        ]
        prepopulated_fields = {'slug': ('Size',)}
        # list_filter = ['is_active','record_status','modified_date']




@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
        list_display = [
        'title','slug','brand_images','discription','is_active',
        # 'created_date','created_id','created_ip','modified_date','modified_id','modified_ip','record_status'
        ]
        # list_filter = ['is_active','record_status','modified_date']
        prepopulated_fields = {'slug': ('title',)}