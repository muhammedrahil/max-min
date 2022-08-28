from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,JsonResponse
from category.models import Category,SubCategory,Brand
from .models import *
from django.template.loader import render_to_string

# # single product deatails

def single_Productdeatail(request,*args,**kwargs):
    try:
        product=SubProductAttribute.objects.get(pk=kwargs.get('single_Productdeatail_pk'))
        productimages=SubProductAttributeImages.objects.filter(product_attribute__pk=kwargs.get('single_Productdeatail_pk'))
        related_product=SubProductAttribute.objects.filter(product__slug=kwargs.get('product_slug')).exclude(pk=kwargs.get('single_Productdeatail_pk'))
        context={
            'product':product,
            'image':productimages,
            'related':related_product,
        }
        return render(request,'user_template/product_deatails/single-product.html',context)
    except:
        raise Http404() 


    