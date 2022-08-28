from django.urls import path
from . import views as v
from . import category as c
app_name = 'productsCategory'

urlpatterns = [

    path('<slug:category_slug>',c.all_categories,name="categories"),
    path('<int:pk>/<int:genter>',c.genter_categories,name="genter_categories"),    
    path('?/filter-data',c.filter_data,name='filter_data'),

    path('<slug:product_slug>/<int:single_Productdeatail_pk>',v.single_Productdeatail,name="single_Productdeatail"),
    

]

