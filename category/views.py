from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .models import *
from django.contrib import messages
from django.views.generic import ListView
from .forms import BrandForm
from .context_processors import get_client_ip
# Create your views here.

def homepage(request):
    return render(request,'user_template/landing_page/homepage.html')

def checkout(request):
    return render(request,'user_template/checkout.html')

def cart(request):
    return render(request,'user_template/cart.html')




# category section ********************/////////////////////***************************

# add category section =========================

def category(request):
    try:
        if request.method == 'POST':
            category=request.POST['category']
            description=request.POST['description']          
            if Category.objects.filter(category=category).exists():
                messages.error(request,'Error:category already exists')
                return redirect('categoryapp:category')
            instence=Category()
            instence.category=category
            instence.description=description
            instence.created_id=request.user
            instence.created_ip=get_client_ip(request)
            instence.save()
            messages.success(request,'Success:category Success fully')
            return redirect('categoryapp:category')
    except:
         messages.error(request,'Error:category already exists')
         return redirect('categoryapp:category')
    context={
        'category': Category.objects.all(),
    }
    return render(request,'admin_template/categories/category/category.html',context)


# edit category =========================

def edit_category(request,pk):
    try:
        if request.method == 'POST':
            category=request.POST['category']
            description=request.POST['description']
            instence=Category.objects.get(pk=pk)
            if instence.category != category :
                if Category.objects.filter(category=category).exists():
                    messages.error(request,'Error:category already exists')
                    return redirect('categoryapp:category')
            instence.category=category
            instence.description=description
            instence.modified_id=request.user
            instence.modified_ip=get_client_ip(request)
            instence.record_status='update'
            instence.save()
            messages.success(request,'Success:Edit Success fully')
            return redirect('categoryapp:category')
        else:
            messages.warning(request,'Warning:category already exists')
            return redirect('categoryapp:category')
    except:
         messages.error(request,'Error:something wrong....')
         return redirect('categoryapp:category')

# delete ajax call 

def delete_category(request):
    pk=request.GET.get('id', None)
    instence=Category.objects.get(pk=pk)
    instence.delete()
    data = {
            'deleted': True
        }   
    return JsonResponse(data)

# active ajax call 

def active_category(request):
    pk=request.GET.get('id', None)
    instence=Category.objects.get(pk=pk)
    if instence.is_active == True:
        instence.is_active=False
        status=False
    else:
        instence.is_active=True
        status=True
    instence.save()
    data = {
        'status':status
    }
    return JsonResponse(data)



# sub category section ********************/////////////////////***************************

# add sub category ========================

class SubCategoryView(ListView):
    model = SubCategory
    template_name = 'admin_template/categories/subcategory/subcategory.html'
    context_object_name = 'sub_category'

    def get_queryset(self, *args, **kwargs):
        return SubCategory.objects.filter(category__is_active=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(is_active=True)
        return context

    def post(self, request, *args, **kwargs):
        try:
            self.category=self.request.POST['category']
            self.sub_category=self.request.POST['sub_category']
            self.description=self.request.POST['description']
            if SubCategory.objects.filter(sub_category=self.sub_category).exists():
                messages.error(request,'Error:sub category already exists')
                return redirect('categoryapp:subcategory')
            instence=SubCategory()
            self.category=Category.objects.get(pk=self.category)
            instence.category=self.category
            instence.sub_category=self.sub_category
            instence.description=self.description
            instence.created_id=self.request.user
            instence.created_ip=get_client_ip(request)
            instence.save()
            messages.success(request,'Success:sub category Success fully')
            return redirect('categoryapp:subcategory')
        except:
            messages.error(request,'Error:something wrong....')
            return redirect('categoryapp:subcategory')


# edit sub category ========================

def edit_sub_category(request,pk):
    try:
        if request.method == 'POST':
            sub_category=request.POST['sub_category']
            description=request.POST['description']
            instence=SubCategory.objects.get(pk=pk)
            if instence.sub_category == sub_category and instence.description == description:
                return redirect('categoryapp:subcategory')
            if instence.sub_category != sub_category :
                if SubCategory.objects.filter(sub_category=sub_category).exists():
                    messages.error(request,'Error:sub category already exists')
                    return redirect('categoryapp:subcategory')
            instence.sub_category=sub_category
            instence.description=description
            instence.modified_id=request.user
            instence.modified_ip=get_client_ip(request)
            instence.record_status='update'
            instence.save()
            messages.success(request,'Success:Edit Success fully')
            return redirect('categoryapp:subcategory')
        else:
            messages.warning(request,'Warning:category already exists')
            return redirect('categoryapp:subcategory')
    except:
         messages.error(request,'Error:something wrong....')
         return redirect('categoryapp:subcategory')


# delete ajax call 

def delete_sub_category(request):
    pk=request.GET.get('id', None)
    instence=SubCategory.objects.get(pk=pk)
    instence.delete()
    data = {
            'deleted': True
        }   
    return JsonResponse(data)

# active ajax call 

def active_sub_category(request):
    pk=request.GET.get('id', None)
    instence=SubCategory.objects.get(pk=pk)
    if instence.is_active == True:
        instence.is_active=False
        status=False
    else:
        instence.is_active=True
        status=True
    instence.save()
    data = {
        'status':status
    }
    return JsonResponse(data)


# size section ********************/////////////////////***************************

# add size ========================

class SizeView(ListView):
    model = Size
    template_name = 'admin_template/categories/size/size.html'
    context_object_name = 'size'

    def get_queryset(self, *args, **kwargs):
        return Size.objects.filter(category__is_active=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(is_active=True)
        return context

    def post(self, request, *args, **kwargs):
        try:
            self.category=self.request.POST['category']
            self.size=self.request.POST['size']
            self.description=self.request.POST['description']
            instence=Size()
            self.category=Category.objects.get(pk=self.category)
            instence.category=self.category
            instence.Size=self.size
            instence.discription=self.description
            instence.created_id=self.request.user
            instence.created_ip=get_client_ip(request)
            instence.save()
            messages.success(request,'Success:Size Success fully')
            return redirect('categoryapp:size')
        except:
            messages.error(request,'Error:something wrong....')
            return redirect('categoryapp:size')

# edit size ========================

def edit_size(request,pk):
    try:
        if request.method == 'POST':
            size=request.POST['size']
            description=request.POST['description']
            instence=Size.objects.get(pk=pk)
            instence.Size=size
            instence.discription=description
            instence.modified_id=request.user
            instence.modified_ip=get_client_ip(request)
            instence.record_status='update'
            instence.save()
            messages.success(request,'Success:Edit Success fully')
            return redirect('categoryapp:size')
        else:
            messages.warning(request,'Warning:something wrong....')
            return redirect('categoryapp:size')
    except:
         messages.error(request,'Error:something wrong....')
         return redirect('categoryapp:size')

# delete ajax call 

def delete_size(request):
    pk=request.GET.get('id', None)
    instence=Size.objects.get(pk=pk)
    instence.delete()
    data = {
            'deleted': True
        }   
    return JsonResponse(data)

# active ajax call 

def active_size(request):
    pk=request.GET.get('id', None)
    instence=Size.objects.get(pk=pk)
    if instence.is_active == True:
        instence.is_active=False
        status=False
    else:
        instence.is_active=True
        status=True
    instence.save()
    data = {
        'status':status
    }
    return JsonResponse(data)


# brand section ********************/////////////////////***************************

def brand(request):
    form=BrandForm()
    return render(request,'admin_template/categories/brand/c.html',{'form':form})