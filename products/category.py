from django.shortcuts import render,get_object_or_404
from django.http import Http404,JsonResponse
from category.models import Category,SubCategory,Brand
from .models import *
from django.core.paginator import Paginator
from django.template.loader import render_to_string


def all_categories(request,*args,**kwargs):
    category = get_object_or_404(Category,slug=kwargs.get('category_slug')) 
    try:
        product=SubProductAttribute.objects.select_related(
        'product','product__product_sub_category',).filter(
        product__is_active=True,product__product_sub_category__category=category)

        subcategory= SubCategory.objects.filter(category=category)
        brands= Brand.objects.filter(brand_category=category)
        size= Size.objects.filter(category=category)
        paginator = Paginator(product, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except SubProductAttribute.DoesNotExist:
        raise Http404()
    context =   {
        "category": category,
        'products' : page_obj,
        'subcategory':  subcategory,
        'brands': brands,
        'size':size
    }
    return render(request,'user_template/category/category.html',context)

def genter_categories(request,*args,**kwargs):
    category = get_object_or_404(Category,pk=kwargs.get('pk'))
    genter= kwargs.get('genter')
    try:
        product=SubProductAttribute.objects.select_related(
        'product','product__product_sub_category',).filter(
        product__is_active=True,product__main_category=genter,product__product_sub_category__category=category)
        subcategory= SubCategory.objects.filter(category=category)
        brands= Brand.objects.filter(brand_category=category)
        size= Size.objects.filter(category=category)
        paginator = Paginator(product, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except SubProductAttribute.DoesNotExist:
        raise Http404()
    context =   {
        "category": category,
        'products' : page_obj,
        'subcategory':  subcategory,
        'brands': brands,
        'size':size
    }
    return render(request,'user_template/category/category.html',context)



# product filter in ajax function 

def filter_data(request):
    categories=request.GET.getlist('subcategory[]')
    brands=request.GET.getlist('brand[]')
    sizes=request.GET.getlist('size[]')
    allProduct=SubProductAttribute.objects.select_related(
        'product','product__product_sub_category',).filter(product__is_active=True)
    print(allProduct)
    if len(categories)>0:
        allProduct=allProduct.filter(product__product_sub_category__id__in=categories)
    print(allProduct)
    if len(brands)>0:
        allProduct=allProduct.filter(product__product_brand__id__in=brands)
    if len(sizes)>0:
        allProduct=allProduct.filter(size__id__in=sizes).distinct()
        
    template =render_to_string('user_template/category/product-list.html',{'data':allProduct})
    return JsonResponse({'data':template})  