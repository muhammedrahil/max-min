

def subcategor_list(request,*args,**kwargs):
    subcategory = get_object_or_404(SubCategory,slug=kwargs.get('subcategory_slug'),category__slug=kwargs.get('category_slug'))
    try:
        product=OfferProducts.objects.select_related('offerProduct','offerProduct__product_sub_category').filter(
            offerProduct__is_active=True,offerProduct__product_sub_category=subcategory)
        paginator = Paginator(product, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except OfferProducts.DoesNotExist:
        raise Http404()
    context =   {
        'products' : page_obj,
        'subcategory' :SubCategory.objects.filter(category=subcategory.category),
        'brands': Brand.objects.filter(brand_category=subcategory.category),
    }
    return render(request,'user_template/category.html',context)



def single_Productdeatail(request,*args,**kwargs):
    # try:
    single_product = OfferProducts.objects.get(pk=kwargs.get('single_Productdeatail_pk'))
    single_product_image = Product.objects.get(slug=kwargs.get('single_Productdeatail_slug'))
    # Product_images = ProductImages.objects.filter(product__slug=kwargs.get('single_Productdeatail_slug'))
    product_attributes=SubProductAttribute.objects.filter(product__slug=kwargs.get('single_Productdeatail_slug'))
    # except Exception as e:
    #     return HttpResponse(e, status=404)
    context =  {
        'single_product' : single_product,
        'single_product_image':single_product_image,
        # 'Product_images':Product_images,
        'product_attributes':product_attributes,
    }
    return render(request,'user_template/single-product.html',context)
    

def single_Product_attribute(request,*args,**kwargs):

    print('***********************************************')
    single_product = OfferProducts.objects.get(offerProduct__slug=kwargs.get('single_Productdeatail_slug'))
    print(single_product,'++++++++++++++++++++++++++')


    # single_product_attribute = ProductAttribute.objects.get(id=kwargs.get('single_Product_attribute_pk'))
    # single_product_images = ProductAttributeImages.objects.filter(product_attribute__pk=kwargs.get('single_Product_attribute_pk'))
    # product_attributes=ProductAttribute.objects.filter(product__slug=kwargs.get('single_Productdeatail_slug'))


    # context =  {
    #     'single_product' : single_product,
    #     'single_product_attribute' :single_product_attribute,
    #     'Product_images':single_product_images,
    #     'product_attributes':product_attributes,
    # }
    return render(request,'user_template/single-product.html')



        function deleteUser(id) {
        var action = confirm("Are you sure you want to delete this user?");
        if (action != false) {
            $.ajax({
                url: '{% url "categoryapp:delete_category" %}',
                data: {
                    'id': id,
                },
                dataType: 'json',
                success: function (data) {
                    if (data.deleted) {
                        $("#userTable #user-" + id).remove();
                        Swal.fire({
                        icon: 'success',
                        title: 'Delete Success fully',
                        showConfirmButton: false,
                        timer: 1500
                    })
                    }
                }
            });
        }
    }




def addsub_category(request, *args, **kwargs):
    if request.method == 'POST':
        category=request.POST['category']
        sub_category=request.POST['sub_category']
        description=request.POST['description']
        if SubCategory.objects.filter(sub_category=sub_category).exists():
            messages.error(request,'Error:sub category already exists')
            return redirect('categoryapp:subcategory')
        instence=SubCategory()
        category=Category.objects.get(pk=category)
        instence.category=category
        instence.sub_category=sub_category
        instence.description=description
        instence.created_id=request.user
        instence.created_ip=get_client_ip(request)
        instence.save()
        messages.success(request,'Success:sub category Success fully')
        return redirect('categoryapp:subcategory')


            path('subcategory/addsub_category',v.addsub_category,name='addsub_category'),
