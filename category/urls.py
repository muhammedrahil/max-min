from django.urls import path
from . import views as v

app_name = 'categoryapp'
urlpatterns = [

    path('',v.homepage,name="homepage"),
    path('checkout',v.checkout,name="checkout"),
    path('cart',v.cart,name="cart"),


# admin
    path('category',v.category,name='category'),
    path('category/<int:pk>',v.edit_category,name='edit_category'),
    path('category/delete',v.delete_category,name='delete_category'),
    path('category/active',v.active_category,name='active_category'),

    path('subcategory/',v.SubCategoryView.as_view(), name='subcategory'),
    path('subcategory/<int:pk>',v.edit_sub_category,name='edit_sub_category'),
    path('subcategory/delete',v.delete_sub_category,name='delete_sub_category'),
    path('subcategory/active',v.active_sub_category,name='active_sub_category'),

    path('size/',v.SizeView.as_view(),name='size'),
    path('size/<int:pk>',v.edit_size,name='edit_size'),
    path('size/delete',v.delete_size,name='delete_size'), 
    path('size/active',v.active_size,name='active_size'), 

    path('brand/',v.brand,name='brand'), 

]